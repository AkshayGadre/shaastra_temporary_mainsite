#!/usr/bin/python
# -*- coding: utf-8 -*-

import global_settings
from global_settings import *
import imp

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#STATIC_URL = os.path.join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# path to erp project
ERP_PROJECT_PATH = '/home/gotham/Webops2014/blh/temp/ERP14/'

# getting the database name of erp for syncing erp dn with mainsite db
erp_global_settings = imp.load_source('global_settings', os.path.abspath( os.path.join( ERP_PROJECT_PATH, 'erp', 'global_settings.py') ) )
erp_local_settings = imp.load_source('local_settings', os.path.abspath( os.path.join( ERP_PROJECT_PATH, 'erp', 'local_settings.py') ) )
erp_db_name = erp_local_settings.DATABASES['default']['NAME']

# *********************** DATABASE DETAILS ADDED ***************
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'random',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'a',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'erp': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': erp_db_name,                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'a',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
SITE_URL="http://localhost:8000/"
# **************************************************************

TEMPLATE_DIRS = (
    os.path.abspath( os.path.join( PROJECT_PATH, 'templates') ),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.abspath( os.path.join( PROJECT_PATH, 'static') ),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.abspath( os.path.join( PROJECT_PATH, 'media') )

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.abspath( os.path.join( PROJECT_PATH, 'static_root') )

#Python's internal mail server settings. FOR DEVELOPMENT ONLY.
#To run the DebuggingServer: python -m smtpd -n -c DebuggingServer localhost:<portnumber>
if DEBUG:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 8000
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = 'root@root.com'


CONTENT_TYPES=['application/pdf',]
MAX_UPLOAD_SIZE=5242880
DEFAULT_FILE_STORAGE =  'django.core.files.storage.FileSystemStorage'

