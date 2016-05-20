#!/usr/bin/env python
# -*- coding: utf-8 -*-


from celery import Celery
from django.conf import settings


# Celery Application
app = Celery(__name__)
app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
