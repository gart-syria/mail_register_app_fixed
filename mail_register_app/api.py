import frappe
from frappe.utils import today, now_datetime

@frappe.whitelist()
def confirm_received(queue_name):

    # 1️⃣ قراءة سجل Queue
    queue = frappe.get_doc("Incoming Confirmation Queue", queue_name)

    if queue.status == "Received":
        return True

    # 2️⃣ تحديث Mail Recipients
    recipient = frappe.get_doc("Mail Recipients", queue.mail_recipient_row)

    recipient.status = "Received"
    recipient.received_confirmed = 1
    recipient.received_date = today()
    recipient.save(ignore_permissions=True)

    # 3️⃣ قراءة البريد الصادر
    outgoing = frappe.get_doc("Mail Register", queue.mail_register)

    # 4️⃣ إنشاء بريد وارد جديد
    incoming = frappe.new_doc("Mail Register")
    incoming.mail_type = "Incoming"
    incoming.direction = "Incoming"
    incoming.subject = outgoing.subject
    incoming.summary = outgoing.summary
    incoming.issuing_office = outgoing.issuing_office
    incoming.receiver_office = queue.recipient_office
    incoming.mail_date = today()
    incoming.received_date = today()
    incoming.linked_outgoing_mail = outgoing.name
    incoming.linked_central_number = outgoing.mail_number
    incoming.status = "Received"
    incoming.insert(ignore_permissions=True)

    # 5️⃣ تحديث Queue
    queue.status = "Received"
    queue.received_confirmed=1
    queue.confirmed_by = frappe.session.user
    queue.confirmed_on = now_datetime()
    queue.save(ignore_permissions=True)

    # 6️⃣ تحديث حالة البريد الصادر إن اكتمل الاستلام
    all_received = True
    for r in outgoing.recipients:
        if r.status != "Received":
            all_received = False
            break

    if all_received:
        outgoing.status = "Received"
        outgoing.save(ignore_permissions=True)

    return True

@frappe.whitelist()
def get_user_diwan(user=None):
    """Return user's Diwan based on User Diwan Mapping."""
    user = user or frappe.session.user
    diwan = frappe.db.get_value(
        "User Diwan Mapping",
        {"user": user},
        "diwan"
    )
    return diwan
