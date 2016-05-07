#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class Site(models.Model):
    """
    Site model.
    """
    title = models.CharField('title',
            max_length=255,
            help_text='Title of the site.')
    url = models.URLField('URL',
            max_length=255, null=False, blank=False,
            help_text='URL of the site.')
    added_time = models.DateTimeField('Added time',
            default=timezone.now,
            help_text='Datetime when the site is added')
    is_visible = models.BooleanField('Visibility',
            default=True, null=False,
            help_text='Whether the site is visible.')

    def __str__(self):
        return self.title