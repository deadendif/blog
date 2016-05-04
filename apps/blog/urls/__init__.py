#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('blog.urls.archives', namespace='entry_archives')),
    url(r'^', include('blog.urls.entries', namespace='entry_detail')),
    url(r'^category/', include('blog.urls.categories', namespace='categories')),
    url(r'^tag/', include('blog.urls.tags', namespace='tags')),
]