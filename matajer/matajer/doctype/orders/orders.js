// Copyright (c) 2016, Ghadeer and contributors
// For license information, please see license.txt

frappe.ui.form.on('orders', {
	save: function(frm) {
         frappe.call({
                method: "apps1.apps1.doctype.matajer.add_order",
                args: {

                },
            callback: function (data) {

            }
            });
	}
});
