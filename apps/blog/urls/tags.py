#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from ..views.tags import TagDetail

urlpatterns = [
    url(r'^(?P<tag>[^/]+(?u))/page/(?P<page>\d+)$',
        TagDetail.as_view(),
        name='detail_paginated'),
    url(r'^(?P<tag>[^/]+(?u))/$', TagDetail.as_view(), name='detail'),
]