#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from blog.views.test import TestView
from blog.views.archives import EntryIndex, EntryYear, EntryMonth

urlpatterns = [
    url(r'^$', TestView.as_view(), name='test_view'),

    url(r'^index/$', EntryIndex.as_view(), name='test_index'),
    url(r'^page/(?P<page>\d+)/$',
        EntryIndex.as_view(),
        name='entry_archive_index_paginated'),

    url(r'^(?P<year>\d{4})/$', EntryYear.as_view(), name='test_year'),
    url(r'^(?P<year>\d{4})/page/(?P<page>\d+)/$',
        EntryYear.as_view(),
        name='entry_archive_year_paginated'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', EntryMonth.as_view(), name='test_month'),
    url(r'^(?P<year>\d{4})/page/(?P<page>\d+)/$',
        EntryYear.as_view(),
        name='entry_archive_year_paginated'),
]