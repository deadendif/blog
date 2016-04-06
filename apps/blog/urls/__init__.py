#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('blog.urls.archives', namespace='entry_archives')),
    url(r'^', include('blog.urls.entries', namespace='entry_detail')),
]