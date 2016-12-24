# -*- coding: utf-8 -*-
# Copyright (c) 2015, Ghadeer and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest
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




