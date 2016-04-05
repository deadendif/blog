#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateResponseMixin

from callable_queryset import CallableQuerysetMixin
from blog.settings import PAGINATION, ALLOW_EMPTY
from blog.models import Entry

class ArchiveMixin(object):
    """
    Mixin centralizing the configuration of the archives views.
    """
    paginate_by = PAGINATION
    allow_empty = ALLOW_EMPTY
    date_field = 'create_time'
    template_name = 'blog/test.html'
    context_object_name = 'entry_list'
    make_object_list = True
    month_format = '%m'
    week_format = '%W'


class EntryArchiveMixin(ArchiveMixin, CallableQuerysetMixin, TemplateResponseMixin):
    """
    Mixin of all archives.
    """
    queryset = Entry.published.all