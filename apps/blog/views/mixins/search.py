#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateResponseMixin
from django.views.generic.list import BaseListView

from .archives import ArchiveConfMixin
from ...settings import MIN_KEYWORD_LENGTH
from ...models import Entry


class EntrySearchMixin(ArchiveConfMixin, BaseListView, TemplateResponseMixin):
    """
    Mixin of entry search.
    """
    pattern = ''
    error = None

    def get_queryset(self):
        """
        [Override] Retrieve search queryset.
        """
        entries = Entry.published.none()

        self.pattern = self.kwargs['pattern']
        if self.pattern:
            if len(self.pattern) < MIN_KEYWORD_LENGTH:
                self.error = 'The pattern is too short.'
            else:
                entries = Entry.published.search(self.pattern)
        return entries

    def get_context_data(self, **kwargs):
        """
        [Override] Update context data when rendering.
        """
        context = super(EntrySearchMixin, self).get_context_data(**kwargs)
        context.update({'error': self.error, 'pattern': self.pattern})
        context.update(getattr(self, 'private_context_data', {}))
        print context
        return context
