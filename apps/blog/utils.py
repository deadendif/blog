#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import logging
import datetime
import markdown as md
from django.db.models import Q
from django.utils import timezone
from django.core.urlresolvers import reverse, resolve
from tagging.models import Tag

from .settings import PUBLISHED
from .settings import MARKDOWN_EXTENSIONS
from .breadcrumbs import Link

logger = logging.getLogger('file')

def entries_published(queryset):
    """
    Return the published entries.
    """
    now = timezone.now()
    return queryset.filter(
        Q(start_publish__lte=now) | Q(start_publish=None),
        Q(end_publish__gt=now) | Q(end_publish=None),
        status=PUBLISHED)


def entries_of_month(queryset, year, month):
    """
    Return entries published in the month.
    """
    start = datetime.datetime(year, month, 1)
    end = datetime.datetime(year + month / 12, (month + 1) % 12, 1)
    return entries_published(queryset).filter(
        create_time__gte=start, create_time__lt=end)


def entry_tags(entry):
    """
    Return the tags of the entry.
    """
    return [Link(tag.name, reverse('blog:tags:detail', args=[tag.name]))
            for tag in Tag.objects.get_for_object(entry)]


def category_ancestors(category, ascending=False, include_self=True, disable_last_url=True):
    """
    Return the ancestors of the category.
    """
    ancestors = [Link(cg.title, cg.get_absolute_url()) for cg in category.get_ancestors(
        ascending=ascending, include_self=include_self)]
    if disable_last_url and ancestors:
        ancestors[-1].disable_url()
    return ancestors


def category_children(category):
    """
    Return the children category of the category.
    """
    return [Link(cg.title, cg.get_absolute_url()) for cg in category.children.all()]


def markdown(text, extensions=MARKDOWN_EXTENSIONS):
    """
    Return html content.
    """
    return md.markdown(text, extensions=extensions)


def recent_year_month(month_delta=0):
    """
    Return the year and the month 'month_delta' months ago.
    """
    year = time.localtime().tm_year
    month = time.localtime().tm_mon - month_delta
    while month < 1:
        year -= 1
        month += 12
    return year, month


def valid_month(year):
    """
    Return available month of the year.
    """
    MONTH_LIST = range(1, 13)
    c_year = time.localtime().tm_year
    year_map = {
        -1: MONTH_LIST,
        0: MONTH_LIST[:time.localtime().tm_mon],
        1: []
    }
    return year_map[cmp(int(year), c_year)]


def extract(request, delim=' ', item_format='[%s=%s]'):
    """
    Extract params from request for log.
    """

    def __extract(method, items):
        if not items:
            return ''
        return method + delim + delim.join(item_format % (k,v) for k, v in items)

    match = resolve(request.path)
    params = {
        'URL' : match.kwargs.items(),
        'GET' : request.GET.items(),
        'POST': request.POST.items()
    }
    return delim.join([p for p in [__extract(method, items) for method, items in params.items()] if p])
