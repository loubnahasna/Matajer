# -*- coding: utf-8 -*-
# Copyright (c) 2015, loubna and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, jwt
from frappe.model.document import Document


class users(Document):
    pass


@frappe.whitelist(allow_guest=True)
def test_token(token):
    try:
        frappe.db.begin()
        secret = "louhashkey123"
        flag = False
        code = jwt.decode(token, secret)
        userid = code['userid']
        list = frappe.get_list('users', filters=[["users", "name", "=", userid]])
        if len(list) == 1:
            flag = True
        frappe.db.commit()
        return {
            "result": flag
        }
    except Exception as e:
        try:
            frappe.db.rollback()
        except:
            pass
        return {
            "result": False
        }


@frappe.whitelist(allow_guest=True)
def register(fullname, username, password):
    try:
        frappe.db.begin()

        secret = "louhashkey123"
        frappe.db.begin()
        users = frappe.get_doc({
            "doctype": "users",
            "fullname": fullname,
            "username": username,
            "password": password

        })
        users.insert(ignore_permissions=True)
        userid = users.name
        token = jwt.encode({'userid': userid}, secret, algorithm='HS256')

        users = frappe.get_doc('users', userid)
        users.token = token
        users.save(ignore_permissions=True)
        frappe.db.commit()
        return {
            "success": True,
            "data": token
        }
    except Exception as e:
        try:
            frappe.db.rollback()
        except:
            pass
        return {
            "data": False
        }
