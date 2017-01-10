<<<<<<< HEAD
// Copyright (c) 2016, loubna and contributors
// For license information, please see license.txt

frappe.ui.form.on('orders', {
	refresh: function(frm) {

=======
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
>>>>>>> 7880af29cfd90e766ac20e5108c5491f3c7cdac6
	}
});
