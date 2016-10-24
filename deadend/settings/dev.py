#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import logging
import logging.config

from os.path import join
from common import *
from settings import *

logging.config.fileConfig(LOG_CONF_PATH, disable_existing_loggers=False,
        defaults={'logfilename': LOG_ONLINE_FILE_PATH, 'name': 'online'})

# #########################################################

# ##### DEBUG CONFIGURATION ###############################
# DEBUG = True
DEBUG = False


# ##### DEBUG CONFIGURATION ###############################
ALLOWED_HOSTS = '*'


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
    'about',
]

INSTALLED_APPS = DEFAULT_APPS + CUSTOM_APPS


######################### OVERRIDE ########################
USE_TZ = False

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

########################## EMAIL ##########################
EMAIL_HOST          = 'smtp.163.com'
EMAIL_PORT          = 25
EMAIL_HOST_USER     = 'noreplyThanks@163.com'
EMAIL_HOST_PASSWORD = base64.b64decode('Z29vZGJ5ZWE=')


######################## MANAGERS #########################
ADMINS = (
    ('deadend', 'deadend.endif@gmail.com'),
    ('deadend', 'deadend.endif@qq.com'),
)

MANAGERS = ADMINS


######################### HTTPS ##########################
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
