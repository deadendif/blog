#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include


urlpatterns = [
    url(r'^category/', include('blog.urls.categories', namespace='categories')),
    url(r'^tag/', include('blog.urls.tags', namespace='tags')),
    url(r'^search/', include('blog.urls.search', namespace='search')),
    url(r'^', include('blog.urls.archives', namespace='archives')),
    url(r'^', include('blog.urls.entries', namespace='entries')),
]