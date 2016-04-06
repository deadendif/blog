#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateResponseMixin

from entries import EntryTimeConfMixin
from callable_queryset import CallableQuerysetMixin
from blog.settings import PAGINATION, ALLOW_EMPTY
from blog.models import Entry

class ArchiveConfMixin(EntryTimeConfMixin):
    """
    Mixin centralizing the configuration.
    """
    paginate_by = PAGINATION
    allow_empty = ALLOW_EMPTY
    template_name = 'blog/archives.html'
    context_object_name = 'entry_list'
    make_object_list = True


class EntryArchiveMixin(ArchiveConfMixin, CallableQuerysetMixin, TemplateResponseMixin):
    """
    Mixin of all archives.
    """
    queryset = Entry.published.all