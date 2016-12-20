import frappe
import frappe.defaults
import unittest
import __init__.py

# load test records and dependencies
# test_records = frappe.get_test_records('Event')

class TestOrders(unittest.TestCase):
    def test_add_order(self):
        add_order_test = add_order(0000, 0000,"Unpaid","AAA", 0000, "d.jpg")

