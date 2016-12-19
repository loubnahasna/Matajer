# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

__version__ = '0.0.1'

@frappe.whitelist(allow_guest=True)
def add_order(order_price,customer_id,status,product_name,product_price,product_image):
    order = frappe.get_doc({
        "doctype":"orders",
        "order_price": order_price,
        "customer_id": customer_id,
        "status": status,
        "products":[{
            "product_name": product_name,
            "product_price":product_price,
            "product_image":product_image
        }]
    })

    order.insert(ignore_permissions = True)

@frappe.whitelist(allow_guest= True)
def update_order(order_name,order_price,customer_id,status,product_name,product_price,product_image):

    ord = frappe.get_doc("orders","%s" % (order_name))
    ord.order_price = order_price
    ord.customer_id = customer_id
    ord.status = status

    for t in ord.get("products"):
        if(t.product_name == product_name):
          t.product_name = product_name
          t.product_price = product_price
          t.product_image = product_image


    ord.save()


#    ord.products[0].product_name = product_name
#    ord.products[0].product_price = product_price
#    ord.products[0].product_image = product_image