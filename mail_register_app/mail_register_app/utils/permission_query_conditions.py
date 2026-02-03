
import frappe

#Filter mails according to user
def filter_mails_according_to_user(user):
	# Check System Manager role using DB (safe_exec compatible)
	is_system_manager = frappe.db.exists(
		"Has Role",
		{
			"parent": user,
			"role": "System Manager"
		}
	)

	if is_system_manager:
		conditions = "1=1"
	else:
		diwan = frappe.db.get_value(
			"User Diwan Mapping",
			{"user": user},
			"diwan"
		)

		if not diwan:
			conditions = "1=0"
		else:
			conditions = f"""
			(
				(
					`tabMail Register`.`mail_type` = 'Outgoing'
					AND `tabMail Register`.`issuing_office` = '{diwan}'
				)
				OR
				(
					`tabMail Register`.`mail_type` = 'Incoming'
					AND `tabMail Register`.`receiver_office` = '{diwan}'
				)
			)
			"""
	
	return conditions

#Filter Waiting Mails Acording to User
def filter_waiting_mails_according_to_user(user):
	user = frappe.session.user
	# System Manager يرى كل شيء
	is_system_manager = frappe.db.exists("Has Role", {"parent": user, "role": "System Manager"})

	if is_system_manager:
		conditions = "1=1"
	else:
		# جلب ديوان المستخدم
		diwan = frappe.db.get_value(
			"User Diwan Mapping",
			{"user": user},
			"diwan"
		)

		if not diwan:
			conditions = "1=0"
		else:
			conditions = (
				"`tabIncoming Confirmation Queue`.`recipient_office` = "
				f"'{diwan}'"
			)

	return conditions
