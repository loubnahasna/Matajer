# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Copyright (c) 2015, loubna and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, json
from frappe.model.document import Document


class orders(Document):
    pass

@frappe.whitelist(allow_guest=True)
def set_order(order_price, customer_id, status, product_list):
    try:

        list1 = json.loads(product_list)

        frappe.db.begin()
        orders = frappe.get_doc({
            "doctype": "orders",
            "order_price": order_price,
            "customer_id": customer_id,
            "status": status

        })
        orders.insert(ignore_permissions=True)
        orderid = orders.name
        price = 0.0
        for list11 in list1:
            order_products = frappe.get_doc({
                "doctype": "order_products",
                "note": list11['note'],
                "price": list11['price'],
                "quantity": list11['quantity'],
                "product_id": list11['product_id'],
                "insert_date": "",
                "parenttype": "orders",
                "parent": orderid
            })
            order_products.insert(ignore_permissions=True)
            price += float(list11['price'])

        orders = frappe.get_doc('orders', orderid)
        orders.order_price = price
        orders.save(ignore_permissions=True)
        frappe.db.commit()
        return {
            "success": True,
            "data": orders
        }
    except Exception as e:
        try:
            frappe.db.rollback()
        except:
            pass
        return {
            "data": False
        }


@frappe.whitelist(allow_guest=True)
def update_order(order_id, product_list):
    try:

        list1 = json.loads(product_list)

        frappe.db.begin()
        price = 0.0
        for list11 in list1:
            products = frappe.get_list('order_products',
                                       filters=[["order_products", "product_id", "=", list11['product_id']],
                                                ["order_products", "parent", "=", order_id]])
            if list11['type'] == "Ins" and len(products) == 0:
                order_products = frappe.get_doc({
                    "doctype": "order_products",
                    "note": list11['note'],
                    "price": list11['price'],
                    "quantity": list11['quantity'],
                    "product_id": list11['product_id'],
                    "insert_date": "",
                    "parenttype": "orders",
                    "parent": order_id
                })
                order_products.insert(ignore_permissions=True)
                price += float(list11['price'])

            if (list11['type'] == "Up" and len(products) == 1) or (list11['type'] == "Ins" and len(products) == 0):
                order_products = frappe.get_doc('order_products', products[0].name)
                order_products.note = list11['note']
                order_products.price = list11['price']
                order_products.quantity = list11['quantity']
                order_products.save(ignore_permissions=True)
                price += float(list11['price'])

            if list11['type'] == "Del":
                frappe.get_doc('order_products', products[0].name).delete_key(products[0].name)

        orders = frappe.get_doc('orders', order_id)
        orders.order_price = price
        orders.save(ignore_permissions=True)
        frappe.db.commit()
        return {
            "success": True,
            "data": orders
        }
    except Exception as e:
        try:
            frappe.db.rollback()
        except:
            pass
        return {
            "data": False
        }

=======
# Copyright (c) 2015, Ghadeer and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class orders(Document):
	pass
>>>>>>> 7880af29cfd90e766ac20e5108c5491f3c7cdac6


