#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db.models import Q
from django.utils import timezone

from settings import PUBLISHED

def entries_published(queryset):
    """
    Return the published entries.
    """
    now = timezone.now()
    return queryset.filter(
        Q(start_publish__lte=now) | Q(start_publish=None),
        Q(end_publish__gt=now) | Q(end_publish=None),
        status=PUBLISHED)