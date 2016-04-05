#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import Q
from django.utils import timezone

from settings import DRAFT, HIDDEN, PUBLISHED
from utils import entries_published

class EntryPublishedManager(models.Manager):
    """
    Manager to retrieve published enteries.
    """

    def get_queryset(self):
        """
        Return published entries
        """
        now = timezone.now()
        return entries_published(super(EntryPublishedManager, self).get_queryset())

    def search(self, pattern):
        """
        Search entries by pattern.
        """
        pass

    def simple_search(self, pattern):
        """
        Simple search for entries.
        """
        pass

    def advanced_search(self, pattern):
        """
        Advanced search for entries.
        """
        pass

