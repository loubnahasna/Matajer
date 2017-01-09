# -*- coding: utf-8 -*-
# Copyright (c) 2015, loubna and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe,requests,httplib
from frappe.model.document import Document


class products(Document):
    pass



def send_telegram(doc, method):
    s="https://api.telegram.org/bot300900133:AAHb8vNP-HHogE1KTATDxGNKip6v8-h_VdI/sendMessage?chat_id=-196752600&text=new product("+doc.name+") have been add to store"
    r= requests.post(s)
    print(r.status_code, r.reason)





@frappe.whitelist(allow_guest=True)
def set_products(product_id,product_name,price):
    try:
        frappe.db.begin()
        products = frappe.get_doc({
            "doctype": "products",
            "product_id": product_id,
            "product_name": product_name,
            "price": price

        })
        products.insert(ignore_permissions=True)
        frappe.db.commit()
        return {
            "success": True,
            "data": products
        }
    except Exception as e:
        try:
            frappe.db.rollback()
        except:
            pass
        return {
            "data": False
        }






