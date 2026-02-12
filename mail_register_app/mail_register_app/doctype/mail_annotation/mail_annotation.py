# Copyright (c) 2026, GARTSYRIA and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MailAnnotation(Document):
    pass
	# def after_insert(self):
	# 	self._add_notes_to_mail_recipient()

	# def before_save(self):
	# 	self._track_updating_of_notes()

	# def _add_notes_to_mail_recipient(self):
	# 	"""Add Notes to Mail Recipient - sync annotation to recipient row."""
	# 	incoming = frappe.get_doc("Mail Register", self.mail_register)
	# 	if not incoming.linked_outgoing_mail:
	# 		return

	# 	outgoing = frappe.get_doc("Mail Register", incoming.linked_outgoing_mail)
	# 	for r in outgoing.recipients:
	# 		if r.recipient_office == incoming.receiver_office:
	# 			self.recipient_office = r.recipient_office
	# 			r.notes = self.annotation_text
	# 			break

	# 	self.db_update()
	# 	outgoing.save(ignore_permissions=True)

	# def _track_updating_of_notes(self):
	# 	"""Track Updating of Notes - create Mail Annotation History on change."""
	# 	old = self.get_doc_before_save()
	# 	if not old or old.annotation_text == self.annotation_text:
	# 		return

	# 	frappe.get_doc(
	# 		{
	# 			"doctype": "Mail Annotation History",
	# 			"parent_annotation": self.name,
	# 			"old_annotation_text": old.annotation_text,
	# 			"modified_by": frappe.session.user,
	# 			"modified_on": frappe.utils.now(),
	# 			"version": old.version or 1,
	# 		}
	# 	).insert(ignore_permissions=True)

	# 	self.version = (old.version or 1) + 1
	# 	self.is_current = 1

	# 	incoming = frappe.get_doc("Mail Register", self.mail_register)
	# 	if incoming.linked_outgoing_mail:
	# 		outgoing = frappe.get_doc("Mail Register", incoming.linked_outgoing_mail)
	# 		for r in outgoing.recipients:
	# 			if r.recipient_office == self.recipient_office:
	# 				r.notes = self.annotation_text
	# 				break
	# 		outgoing.save(ignore_permissions=True)
