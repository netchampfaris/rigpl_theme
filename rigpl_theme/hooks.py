# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "rigpl_theme"
app_title = "RIGPL Theme"
app_publisher = "Frappe Technologies Pvt. Ltd."
app_description = "Theme for RIGPL Website"
app_icon = "octicon octicon-file-media"
app_color = "orange"
app_email = "hello@frappe.io"
app_license = "MIT"
hide_in_installer = True
home_page = "index"

website_context = {
	"disable_website_theme": True
}

controller_context = {
	'Item': 'rigpl_theme.templates.generators.item'
}
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rigpl_theme/css/rigpl_theme.css"
# app_include_js = "/assets/rigpl_theme/js/rigpl_theme.js"

# include js, css files in header of web template
# web_include_css = "/assets/rigpl_theme/css/rigpl_theme.css"
# web_include_js = "/assets/rigpl_theme/js/rigpl_theme.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "rigpl_theme.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rigpl_theme.install.before_install"
# after_install = "rigpl_theme.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rigpl_theme.notifications.get_notification_config"

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

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rigpl_theme.tasks.all"
# 	],
# 	"daily": [
# 		"rigpl_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"rigpl_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rigpl_theme.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rigpl_theme.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rigpl_theme.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rigpl_theme.event.get_events"
# }

