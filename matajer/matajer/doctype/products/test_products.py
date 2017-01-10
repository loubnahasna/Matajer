# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Copyright (c) 2015, loubna and Contributors
=======
# Copyright (c) 2015, Ghadeer and Contributors
>>>>>>> 7880af29cfd90e766ac20e5108c5491f3c7cdac6
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest
<<<<<<< HEAD


# test_records = frappe.get_test_records('products')

class Testproducts(unittest.TestCase):

    def test_set_products(self):
     expected_values = [
        {
            "product_id": "10",
            "product_name": "pro-1",
            "price": 10

        },
        {
            "product_id": "11",
            "product_name": "pro-2",
            "price": 10

        },
        {
            "product_id": "12",
            "product_name": "pro-3",
            "price": 10

        }

    ]
     flag = True




     for i in range(len(expected_values)):
        item = expected_values[i]
        products = frappe.get_doc({
            "doctype": "products",
            "product_id": item['product_id'],
            "product_name": item['product_name'],
            "price": item['price']
        })
        products.insert(ignore_permissions=True)
        n1 = products.name
        list = frappe.get_list('products', filters=[["products", "name", "=", n1]])
        if len(list) == 0:
            flag = False

     self.assertTrue(flag)


=======
from productsLogic import add_product
from productsLogic import update_product

test_records = frappe.get_test_records('products')

class Testproducts(unittest.TestCase):
	def test_add_product(self):
		add_product("ORD-00002","unit-test",111,"unit-test.png")

		ord = frappe.get_doc("orders", "ORD-00002")

		lenghtOfProducts = len(ord.get("products"))

		list1 = []

		for product in ord.get("products"):
			if product == ord.products[lenghtOfProducts-1]:
				list1 ={
					'product_name': product.product_name,
					'product_price': product.product_price,
					'product_image':product.product_image
				}

		self.assertEqual(ord.products[lenghtOfProducts-1].product_name, list1['product_name'])
		self.assertEqual(ord.products[lenghtOfProducts - 1].product_price, list1['product_price'])
		self.assertEqual(ord.products[lenghtOfProducts - 1].product_image, list1['product_image'])
#		self.assertEqual(product, list1)

	def test_update_product(self):
		product_id = 'c29e97ad52'

		beforeU = frappe.get_doc("products", product_id)
		updated_name = "unit"
		updated_price = "55555555555"
		updated_image = "uuuuu.png"

		update_product(updated_name,updated_price,updated_image,product_id)

#		AfterU = frappe.get_doc("products", product_id)

#		self.assertEqual(beforeU.product_name, AfterU.product_name)
#		self.assertEqual(beforeU.product_price, AfterU.product_price)
#		self.assertEqual(beforeU.product_image, AfterU.product_image)
>>>>>>> 7880af29cfd90e766ac20e5108c5491f3c7cdac6




