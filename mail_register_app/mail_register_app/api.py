import frappe

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
