#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..breadcrumbs import Link
from .mixins.search import EntrySearchMixin


class EntrySearch(EntrySearchMixin):
    """
    Entry search view.
    """

    @property
    def private_context_data(self):
        """
        Private context data: breadcrumbs.
        """
        ttl = u'[搜索] %s' % self.pattern 
        return {'ttl': ttl, 'breadcrumbs': [Link('Search : %s' % self.pattern)], 'labels': []}
