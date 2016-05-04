#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db.models import Q
from django.utils import timezone
from django.core.urlresolvers import reverse
from tagging.models import Tag

from settings import PUBLISHED
from breadcrumbs import Link

def entries_published(queryset):
    """
    Return the published entries.
    """
    now = timezone.now()
    return queryset.filter(
        Q(start_publish__lte=now) | Q(start_publish=None),
        Q(end_publish__gt=now) | Q(end_publish=None),
        status=PUBLISHED)

def entry_tags(entry):
    """
    Return the tags of the entry.
    """
    return [Link(tag.name, reverse('blog:tags:detail', args=[tag.name])) for tag in Tag.objects.get_for_object(entry)]


def category_ancestors(category, ascending=False, include_self=True, disable_last_url=True):
    """
    Return the ancestors of the category.
    """
    ancestors = [Link(cg.title, cg.get_absolute_url()) for cg in category.get_ancestors(ascending=ascending, include_self=include_self)]
    if disable_last_url and ancestors:
        ancestors[-1].disable_url()
    return ancestors

def category_children(category):
    """
    Return the children category of the category.
    """
    return [Link(cg.title, cg.get_absolute_url()) for cg in category.children.all()]