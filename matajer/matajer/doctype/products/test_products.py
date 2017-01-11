# -*- coding: utf-8 -*-
# Copyright (c) 2015, loubna and Contributors


from __future__ import unicode_literals

import frappe
import unittest
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




