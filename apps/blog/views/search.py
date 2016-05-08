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
        return {'breadcrumbs': [Link('Search : %s' % self.pattern)], 'labels': []}
