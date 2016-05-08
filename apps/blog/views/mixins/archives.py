#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateResponseMixin

from .entries import EntryTimeConfMixin
from .callable_queryset import CallableQuerysetMixin
from ...settings import PAGINATION, ALLOW_EMPTY
from ...models import Entry

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

    def get_context_data(self, **kwargs):
        """
        [Override] Update context data when rendering.
        """
        context = super(EntryArchiveMixin, self).get_context_data(**kwargs)
        # context.update(self.public_context_data)
        context.update(getattr(self, 'private_context_data', {}))
        return context
