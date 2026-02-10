// Copyright (c) 2026, GARTSYRIA and contributors
// For license information, please see license.txt

frappe.ui.form.on("Incoming Confirmation Queue", {
	received_confirmed(frm) {
		if (!frm.doc.received_confirmed) return;

		frappe.confirm(
			__("هل تريد تأكيد استلام هذا البريد وإنشاء بريد وارد؟"),
			() => {
				frappe.call({
					method: "mail_register_app.api.confirm_received",
					args: { queue_name: frm.doc.name },
					callback: function (r) {
						if (r.message) {
							frappe.show_alert({
								message: "✅ تم تأكيد الاستلام وإنشاء البريد الوارد",
								indicator: "green"
							});
							frm.reload_doc();
						}
					}
				});
			},
			() => { frm.set_value("received_confirmed", 0); }
		);
	}
});
