# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "matajer"
app_title = "matajer"
app_publisher = "loubna"
app_description = "orders and products"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "loubna.hasna@exa.com.sa"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/matajer/css/matajer.css"
# app_include_js = "/assets/matajer/js/matajer.js"

# include js, css files in header of web template
# web_include_css = "/assets/matajer/css/matajer.css"
# web_include_js = "/assets/matajer/js/matajer.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "matajer.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "matajer.install.before_install"
# after_install = "matajer.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "matajer.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }


doc_events = {
    "products": {
        "after_insert": "matajer.matajer.doctype.products.products.send_telegram",
    }
 }



# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"matajer.tasks.all"
# 	],
# 	"daily": [
# 		"matajer.tasks.daily"
# 	],
# 	"hourly": [
# 		"matajer.tasks.hourly"
# 	],
# 	"weekly": [
# 		"matajer.tasks.weekly"
# 	]
# 	"monthly": [
# 		"matajer.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "matajer.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "matajer.event.get_events"
# }

