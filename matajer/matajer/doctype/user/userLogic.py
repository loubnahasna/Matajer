from __future__ import unicode_literals
import frappe
from jose import jwt


@frappe.whitelist(allow_guest=True)
def set_token(first_name,last_name,password,email):

    exist = frappe.db.exists("User",email)
    user = frappe.get_doc({
        "doctype": "User",
        "first_name": first_name,
        "last_name": last_name,
        "new_password": password,
        "email": email
      })

    if  not exist:
        user.insert(ignore_permissions = True)

    frappe_user = frappe.get_doc("User", email)
    user_id = frappe_user.frappe_userid

    user_token = jwt.encode({'frappe_userid': user_id}, 'secret', algorithm='HS256')
    u'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ2YWx1ZSJ9.FG-8UppwHaFp1LgRYQQeS6EDQF7_6-bMFegNucHjmWg'

    return user_token



@frappe.whitelist(allow_guest=True)
def login(user_token):
    decoded = jwt.decode(user_token, 'secret', algorithms=['HS256'])
    {u'frapee_userid': u'user_id'}

    real_user = frappe.db.exists("User", decoded)

    if not real_user:
        return False
    else:
        return True




