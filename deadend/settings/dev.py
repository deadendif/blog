#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
# Import some utility functions
from os.path import join
# Fetch our common settings
from common import *

# #########################################################

# ##### DEBUG CONFIGURATION ###############################
DEBUG = True


# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': join(PROJECT_ROOT, 'run', 'dev.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'deadend',
        'USER': 'deadend',
        'PASSWORD': base64.b64decode('Z29vZGJ5ZWE='),
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}

# ##### APPLICATION CONFIGURATION #########################
CUSTOM_APPS = [
    'mptt',
    'tagging',
    'blog',
]

INSTALLED_APPS = DEFAULT_APPS + CUSTOM_APPS
