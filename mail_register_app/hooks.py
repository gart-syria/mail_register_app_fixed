app_name = "mail_register_app"
app_title = "Mail Register App"
app_publisher = "GARTSYRIA"
app_description = "For Diwan"
app_email = "it@ortas.online"
app_license = "mit"


fixtures = [
    # Role
    {
        "dt": "Role",
        "filters": [
            ["name", "in", ["Diwan User"]]
        ]
    },

    # Server Scripts (v15)
    {
        "dt": "Server Script",
        "filters": [
            ["name", "in", [
                "get_user_diwan",
                "Set root Outgoing Mail",
                "Add Notes to Mail Reciepient Doctype with Ability to Update and Tracking",
                "Track Updating of Notes",
                "Filter Waiting Mails Acording to User",
                "Filter mails according to user",
                "Auto Fill Mail Reciepient in Queue",
                "Auto Mail Number"
            ]]
        ]
    },

    # Client Scripts (v15)
    {
        "dt": "Client Script",
        "filters": [
            ["name", "in", [
                "Button For Adding Replay To Mail",
                "Auto Select for Issuing Receiving office if inbox from external entity",
                "Auto Fill Issuing Office",
                "Button To Show Replays",
                "Button For Adding Notes To Mail",
                "Updated Auto Compose Inbox When Recieving Mail",
                "Change Mail Status from Draft to Sent v2"
            ]]
        ]
    },
       # Custom Doctypes
{
    "dt": "Custom Doctype",
    "filters": [
        ["name", "in", [
            "Mail Register",
            "Mail Recipients",
            "External Entity",
            "Mail External Recipients",
            "Diwan",
            "Incoming Confirmation Queue",
           "Mail Annotation",
           "Mail Annotation History",
           "User Diwan Mapping",
            
        ]]
    ]
},
     # Export Custom Fields only for your app's Doctypes (if you have added any)
    {"dt": "Custom Field", "filters": [
        ["dt", "in", [
            "Mail Register",
            "Incoming Confirmation Queue",
            "Mail Recipients",
            "Mail Annotation",
            "Mail Annotation History",
            "User Diwan Mapping",
            "External Entity",
            "Mail External Recipients",
            "Diwan"
            
            
        ]]
    ]},

    # Export Property Setters for your Doctypes (if you modified field properties)
    {"dt": "Property Setter", "filters": [
        ["doc_type", "in", [
            "Mail Register",
            "Incoming Confirmation Queue",
            "Mail Recipients",
            "Mail Annotation",
            "Mail Annotation History",
            "User Diwan Mapping",
            "External Entity",
            "Mail External Recipients",
            "Diwan"
        ]]
    ]}
  
]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "mail_register_app",
# 		"logo": "/assets/mail_register_app/logo.png",
# 		"title": "Mail Register App",
# 		"route": "/mail_register_app",
# 		"has_permission": "mail_register_app.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mail_register_app/css/mail_register_app.css"
# app_include_js = "/assets/mail_register_app/js/mail_register_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/mail_register_app/css/mail_register_app.css"
# web_include_js = "/assets/mail_register_app/js/mail_register_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mail_register_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "mail_register_app/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "mail_register_app.utils.jinja_methods",
# 	"filters": "mail_register_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mail_register_app.install.before_install"
# after_install = "mail_register_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mail_register_app.uninstall.before_uninstall"
# after_uninstall = "mail_register_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "mail_register_app.utils.before_app_install"
# after_app_install = "mail_register_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "mail_register_app.utils.before_app_uninstall"
# after_app_uninstall = "mail_register_app.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mail_register_app.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mail_register_app.tasks.all"
# 	],
# 	"daily": [
# 		"mail_register_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"mail_register_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mail_register_app.tasks.weekly"
# 	],
# 	"monthly": [
# 		"mail_register_app.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "mail_register_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mail_register_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mail_register_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["mail_register_app.utils.before_request"]
# after_request = ["mail_register_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["mail_register_app.utils.before_job"]
# after_job = ["mail_register_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"mail_register_app.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

