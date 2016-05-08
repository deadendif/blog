#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from ..views.categories import CategoryDetail


urlpatterns = [
    url(r'^(?P<path>[-\/\w]+)/page/(?P<page>\d+)/$',
        CategoryDetail.as_view(),
        name="detail_paginated"),
    url(r'^(?P<path>[-\/\w]+)/$', CategoryDetail.as_view(), name="detail"),
]