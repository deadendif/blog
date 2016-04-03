#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from blog.views.test import TestView
from blog.views.entries import EntryDetail

urlpatterns = [
    url(r'^/$', TestView.as_view(), name='test_view'),
]