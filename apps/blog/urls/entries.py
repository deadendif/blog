#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from ..views.entries import EntryDetail

urlpatterns = [
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 
        EntryDetail.as_view(),
        name='detail'),
]
