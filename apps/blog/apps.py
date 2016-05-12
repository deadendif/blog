#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Application configuration.
    """

    name = 'blog'
    verbose_name = 'Blog Application'

    def ready(self):
        import blog.signals
