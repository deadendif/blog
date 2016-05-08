#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from ..views.search import EntrySearch

urlpatterns = [
    url(r'^(?P<pattern>.+?)/page/(?P<page>\d+)/$',
        EntrySearch.as_view(),
        name='index_paginated'),
    url(r'^(?P<pattern>.+?)/$', EntrySearch.as_view(), name='index'),
]