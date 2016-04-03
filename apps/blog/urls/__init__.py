#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include


urlpatterns = [
    url(r'^test/', include('blog.urls.test')),
    # url(r'^', include('blog.urls.entries')),
]