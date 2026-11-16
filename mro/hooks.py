# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "mro"
app_title = "Frappe Aviation Mro Aircraft Maintenance"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Aviation Mro Aircraft Maintenance for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/mro/css/mro.bundle.css"
app_include_js = "/assets/mro/js/mro.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "mro.engine.on_document_submit",
        "on_cancel": "mro.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "mro.engine.daily_scheduled_sync"
    ]
}
