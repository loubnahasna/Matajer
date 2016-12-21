# -*- coding: utf-8 -*-
# Copyright (c) 2015, Ghadeer and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest
from productsLogic import add_product

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

