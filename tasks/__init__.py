#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import logging.config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deadend.settings.production')


from django.conf import settings

logging.config.fileConfig(settings.LOG_CONF_PATH, disable_existing_loggers=False,
        defaults={'logfilename': settings.LOG_CELERY_FILE_PATH, 'name': 'tasks'})

from .app import app
from .about_tasks import *
