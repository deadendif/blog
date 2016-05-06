#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from django import template
from django.core.urlresolvers import reverse
from tagging.models import Tag

from blog.models import Entry
from blog.settings import HASH_TAG_COLOR_START, HASH_TAG_COLOR_END
register = template.Library()


@register.inclusion_tag('tags/_tags_snippet.html')
def get_tags():
    """
    Return all tags's infomation.
    """
    from random import randint
    t_tags = [{
            'title': t.name,
            'url': reverse('blog:tags:detail', args=[t.name]),
            'count': t.count
        } for t in Tag.objects.usage_for_model(Entry, counts=True)]
    return {'t_tags': t_tags}


@register.filter
def size(count):
    """
    Return size according to 'count'.
    """
    BASE = 1
    SIZES = ['mini', 'tiny', 'small', 'medium', 'large', 'big', 'huge', 'massive']
    index = count / BASE if (count / BASE <= len(SIZES) - 1) else (len(SIZES) - 1)
    return SIZES[index]


@register.filter
def color(title):
    """
    Return color according to 'title'.
    """
    COLORS = ['red', 'orange', 'yellow', 'olive', 'green', 'teal', 'blue', 'violet', 'purple', 'pink', 'brown', 'grey', 'black']
    md5 = hashlib.md5()
    md5.update(str(title))
    index = int(md5.hexdigest()[HASH_TAG_COLOR_START:HASH_TAG_COLOR_END], 16) % len(COLORS)
    return COLORS[index]
