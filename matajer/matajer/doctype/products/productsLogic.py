from __future__ import unicode_literals
import frappe

@frappe.whitelist(allow_guest=True)
def add_product(order_name,product_name,product_price,product_image):
    ord = frappe.get_doc("orders", "%s" % (order_name))

    product = {
        "product_name": product_name,
        "product_price": product_price,
        "product_image": product_image
    }

    ord.append("products", product)
    ord.save()


@frappe.whitelist(allow_guest=True)
def update_product(product_name,product_price,product_image,product_id):
    product = frappe.get_doc("products","%s" % (product_id))

    product.product_name = product_name
    product.product_price = product_price
    product.product_image = product_image

    product.save()


