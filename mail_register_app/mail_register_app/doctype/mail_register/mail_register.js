// Copyright (c) 2026, GARTSYRIA and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Mail Register", {
// 	onload(frm) {
// 		// Auto Fill Issuing Office - تحديد خيارات الجهة المرسلة حسب المستخدم
// 		frm.set_query("issuing_office", function () {
// 			return {
// 				query: "frappe.db.get_list",
// 				filters: {
// 					doctype: "User Diwan Mapping",
// 					user: frappe.session.user
// 				}
// 			};
// 		});

// 		if (frm.doc.__islocal === 1 && !frm.doc.issuing_office) {
// 			frappe.call({
// 				method: "frappe.client.get_value",
// 				args: {
// 					doctype: "User Diwan Mapping",
// 					filters: { user: frappe.session.user },
// 					fieldname: "diwan"
// 				},
// 				callback: function (r) {
// 					if (r.message && r.message.diwan) {
// 						frm.set_value("issuing_office", r.message.diwan);
// 					}
// 				}
// 			});
// 		}
// 	},

// 	refresh(frm) {
// 		if (frm.doc.__islocal !== 1) {
// 			frm.set_df_property("issuing_office", "read_only", 1);
// 		}

// 		update_status_based_on_recipients(frm);

// 		if (frm.doc.mail_type === "Incoming" && frm.doc.__islocal !== 1) {
// 			frm.add_custom_button(
// 				__("إضافة حاشية"),
// 				function () {
// 					frappe.new_doc("Mail Annotation", { mail_register: frm.doc.name });
// 				},
// 				__("إجراءات")
// 			);
// 			frm.add_custom_button(
// 				__("الرد بكتاب صادر"),
// 				function () {
// 					create_reply_outgoing(frm);
// 				},
// 				__("إجراءات")
// 			);
// 		}

// 		if (frm.doc.__islocal !== 1) {
// 			frm.add_custom_button(
// 				__("عرض الردود"),
// 				function () { show_replies(frm); },
// 				__("إجراءات")
// 			);
// 		}
// 	},

// 	from_external_entity(frm) {
// 		if (frm.doc.from_external_entity) {
// 			frappe.db.get_value("Diwan", { name1: "الديوان المركزي" }, "name").then((r) => {
// 				if (r && r.message && r.message.name) {
// 					frm.set_value("receiver_office", r.message.name);
// 					frm.set_value("status", "Received");
// 				} else {
// 					frappe.msgprint("⚠️ لم يتم العثور على ديوان باسم 'الديوان المركزي' في الحقل name1");
// 				}
// 			});
// 			frm.set_value("received_date", frappe.datetime.now_date());
// 			frappe.show_alert({
// 				message: "📩 بريد وارد من جهة خارجية — تم تعيين الحالة إلى Received",
// 				indicator: "green"
// 			});
// 		} else {
// 			frm.set_value("receiver_office", "");
// 			frm.set_value("received_date", "");
// 			frm.set_value("status", "Draft");
// 		}
// 	},

// 	recipients_add(frm, cdt, cdn) { update_status_based_on_recipients(frm); },
// 	recipients_remove(frm, cdt, cdn) { update_status_based_on_recipients(frm); },
// 	external_recipients_add(frm, cdt, cdn) { update_status_based_on_recipients(frm); },
// 	external_recipients_remove(frm, cdt, cdn) { update_status_based_on_recipients(frm); },

// 	validate(frm) {
// 		if (!frm.doc.issuing_office) {
// 			frappe.call({
// 				method: "frappe.client.get_value",
// 				args: {
// 					doctype: "User Diwan Mapping",
// 					filters: { user: frappe.session.user },
// 					fieldname: "diwan"
// 				},
// 				callback: function (r) {
// 					if (r.message && r.message.diwan) {
// 						frm.set_value("issuing_office", r.message.diwan);
// 					} else {
// 						frappe.throw(__("لا يوجد ديوان مرتبط بهذا المستخدم"));
// 					}
// 				}
// 			});
// 		}
// 	}
// });

function update_status_based_on_recipients(frm) {
	if (frm.doc.status === "Received") return;
	const has_internal = (frm.doc.recipients || []).length > 0;
	const has_external = (frm.doc.external_recipients || []).length > 0;
	if ((has_internal || has_external) && frm.doc.status !== "Sent") {
		frm.set_value("status", "Sent");
		frappe.show_alert({ message: "تم تحويل حالة البريد إلى (Sent) ✅", indicator: "green" });
	} else if (!has_internal && !has_external && frm.doc.status !== "Draft") {
		frm.set_value("status", "Draft");
		frappe.show_alert({ message: "تمت إعادة الحالة إلى (Draft)", indicator: "orange" });
	}
}

function create_reply_outgoing(frm) {
	frappe.confirm("هل تريد إنشاء كتاب صادر ردًا على هذا البريد؟", () => {
		frappe.new_doc("Mail Register", {
			mail_type: "Outgoing",
			direction: "Outgoing",
			reply_to: frm.doc.name,
			subject: "رد على: " + (frm.doc.subject || ""),
			issuing_office: frm.doc.receiver_office,
			mail_date: frappe.datetime.now_date()
		});
	});
}

function show_replies(frm) {
	if (frm.doc.mail_type === "Incoming") {
		frappe.route_options = { reply_to: frm.doc.name };
		frappe.set_route("List", "Mail Register");
	} else if (frm.doc.mail_type === "Outgoing") {
		frappe.route_options = { mail_type: "Incoming", root_outgoing_mail: frm.doc.name };
		frappe.set_route("List", "Mail Register");
	}
}
