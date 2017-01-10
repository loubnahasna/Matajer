from __future__ import unicode_literals
import frappe,jwt
from frappe.model.document import Document


@frappe.whitelist(allow_guest=True)
def register(fullname,username,password):
    try:
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



