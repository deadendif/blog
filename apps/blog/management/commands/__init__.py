#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import logging.config

from django.conf import settings


logging.config.fileConfig(settings.LOG_CONF_PATH, disable_existing_loggers=False,
        defaults={'logfilename': settings.LOG_OFFLINE_FILE_PATH, 'name': 'offline'})

