#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import Q
from django.utils import timezone

from .settings import DRAFT, HIDDEN, PUBLISHED
from .settings import SEARCH_FIELDS
from .utils import entries_published


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
        return self.simple_search(pattern)
        # try:
        #     return self.advanced_search(pattern)
        # except Exception, e:
        #     return self.simple_search(pattern)

    def simple_search(self, pattern):
        """
        Simple search for entries.
        TODO: Regex search
        """
        query = Q()
        for ptn in pattern.split():
            for field in SEARCH_FIELDS:
                query |= Q(**{'%s__icontains' % field: ptn})
        return self.get_queryset().filter(query)

    def advanced_search(self, pattern):
        """
        Advanced search for entries.
        TODO: Advanced search.
        """
        pass

