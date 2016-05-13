#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from ..models import EntryCounter
from ..caches import EntryCounterCache

register = template.Library()


@register.filter
def entry_counter(entry, ctype):
    """
    Return the count number according to ctype.
    """
    if ctype not in EntryCounter._meta.get_all_field_names():
        raise InvalidCounterTypeException('Invalid type of entry counter, type="%s"' % str(ctype))
 
    entry_counter = EntryCounterCache(entry)
    return entry_counter.get(ctype)
