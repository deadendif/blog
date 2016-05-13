#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from .entry import Entry


class EntryCounter(models.Model):
    """
    Entry counter model.
    """
    entry = models.OneToOneField(Entry,
            null=True, on_delete=models.SET_NULL, unique=True,
            related_name='counter',
            help_text='The entry that counter belongs to.')
    page_view_num = models.IntegerField('page view number',
            default=0,
            help_text='The page view number of the entry.')
    useful_num = models.IntegerField('useful number',
            default=0,
            help_text='The number of people who thinks the entry is useful.')
    useless_num = models.IntegerField('useful number',
            default=0,
            help_text='The number of people who thinks the entry is useful.')

    def __str__(self):
        return '%s: pv=%d, uf=%d, ul=%d' % (self.entry.title, self.page_view_num, self.useful_num, self.useless_num)