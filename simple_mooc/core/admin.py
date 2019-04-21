from django.contrib import admin
import os
import json

SETTING_FILE = open(os.path.dirname(__file__) + '/templates_config/template_teste.json').read()
SITE_CONFIGURATION = json.loads(SETTING_FILE)

admin.site.site_header = SITE_CONFIGURATION['SITE_NAME'] if SITE_CONFIGURATION['SITE_NAME'] else 'Admin Page'
