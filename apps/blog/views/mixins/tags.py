#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import Http404
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.list import BaseListView
from tagging.utils import get_tag
from tagging.models import TaggedItem

from .archives import ArchiveConfMixin
from ...models import Entry


class TagDetailMixin(ArchiveConfMixin, BaseListView, TemplateResponseMixin):
    """
    Mixin of tag detail. 
    """

    def get_queryset(self):
        """
        [Override] Retrieve the tag by its name and get its published entries.
        """
        self.tag = get_tag(self.kwargs['tag'])
        if self.tag is None:
            raise Http404('No such tag: %s' % self.kwargs['tag'])

        return TaggedItem.objects.get_by_model(Entry.published.all(), self.tag)

    def get_context_data(self, **kwargs):
        """
        [Override] Update context data when rendering.
        """
        context = super(TagDetailMixin, self).get_context_data(**kwargs)
        # context['tag'] = self.tag
        context.update(getattr(self, 'private_context_data', {}))
        return context
