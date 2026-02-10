# Copyright (c) 2026, GARTSYRIA and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MailRegister(Document):
	def before_insert(self):
		self._auto_mail_number()
		self._set_root_outgoing_mail()

	def before_save(self):
		self._set_root_outgoing_mail()

	def on_update(self):
		self._auto_fill_mail_recipient_in_queue()

	def _auto_mail_number(self):
		"""Auto Mail Number - generate name for incoming/outgoing mail."""
		year = frappe.utils.nowdate().split("-")[0]
		direction = "OUT" if self.mail_type == "Outgoing" else "IN"

		if direction == "OUT":
			if not self.issuing_office:
				frappe.throw("الرجاء تحديد الجهة المرسلة (Issuing Office) قبل الحفظ.")
			diwan_office = self.issuing_office
		else:
			if not self.receiver_office:
				frappe.throw("الرجاء تحديد الجهة المستقبلة (Receiver Office) قبل الحفظ.")
			diwan_office = self.receiver_office

		diwan_doc = frappe.get_doc("Diwan", diwan_office)
		diwan_code = diwan_doc.code or "UNK"

		pattern = f"{diwan_code}-{direction}-{year}-%"
		existing = frappe.db.get_all(
			"Mail Register",
			filters={"name": ["like", pattern], "docstatus": ["!=", 2]},
			fields=["name"],
		)

		max_num = 0
		for e in existing:
			try:
				num = int(e["name"].split("-")[-1])
				if num > max_num:
					max_num = num
			except Exception:
				pass

		next_num = max_num + 1
		new_name = f"{diwan_code}-{direction}-{year}-{str(next_num).zfill(5)}"
		self.name = new_name
		self.mail_number = new_name

	def _set_root_outgoing_mail(self):
		"""Set Root Outgoing Mail."""
		if self.root_outgoing_mail:
			return
		if self.mail_type == "Outgoing" and not self.reply_to:
			self.root_outgoing_mail = self.name
		elif self.mail_type == "Outgoing" and self.reply_to:
			parent = frappe.get_doc("Mail Register", self.reply_to)
			self.root_outgoing_mail = parent.root_outgoing_mail or parent.name
		elif self.mail_type == "Incoming" and self.linked_outgoing_mail:
			outgoing = frappe.get_doc("Mail Register", self.linked_outgoing_mail)
			self.root_outgoing_mail = outgoing.root_outgoing_mail or outgoing.name

	def _auto_fill_mail_recipient_in_queue(self):
		"""Auto Fill Mail Recipient in Queue - create Incoming Confirmation Queue for sent recipients."""
		doc = frappe.get_doc("Mail Register", self.name)
		if doc.mail_type != "Outgoing":
			return

		for r in doc.recipients:
			if r.status != "Sent":
				continue
			if frappe.db.exists("Incoming Confirmation Queue", {"mail_recipient_row": r.name}):
				continue

			queue = frappe.new_doc("Incoming Confirmation Queue")
			queue.mail_register = doc.name
			queue.mail_recipient_row = r.name
			queue.recipient_office = r.recipient_office
			queue.status = r.status
			queue.mail_number = doc.mail_number
			queue.mail_date = doc.mail_date
			queue.subject = doc.subject
			queue.received_confirmed = 0
			queue.insert(ignore_permissions=True)
