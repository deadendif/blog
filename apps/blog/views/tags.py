#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..breadcrumbs import Link
from .mixins.tags import TagDetailMixin


class TagDetail(TagDetailMixin):
    """
    Tag detail view.
    """

    @property
    def private_context_data(self):
        """
        Private context data: breadcrumbs.
        """
        ttl = u'[标签] %s' % self.tag.name
        return {'ttl': ttl, 'breadcrumbs': [Link('Tag : %s' % self.tag.name)], 'labels': []}