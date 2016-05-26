#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deadend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^super/', include(admin.site.urls)),
    url(r'^blog/', include('apps.blog.urls', namespace='blog')),
    url(r'^about/', include('apps.about.urls', namespace='about')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
