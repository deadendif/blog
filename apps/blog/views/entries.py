#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.dates import BaseDateDetailView

from .mixins.entries import EntryDetailMixin
from ..utils import category_ancestors, entry_tags
from ..breadcrumbs import Link


class EntryDetail(EntryDetailMixin, BaseDateDetailView):
    """
    Entry detail view.
    TODO: entry login and password protections.
    """
    # session_key = 'entry_passwd_%s'

    @property
    def private_context_data(self):
        """
        Private context data: title, breadcrumbs, direct subdirectories.
        """
        ttl = self.object.title
        breadcrumbs = category_ancestors(self.object.category, disable_last_url=False)
        breadcrumbs.append(Link(self.object.title))
        return {'ttl': ttl, 'breadcrumbs': breadcrumbs, 'labels': entry_tags(self.object)}

    # def get(self, request, *args, **kwargs):
    #     """
    #     Validate permission.
    #     """
    #     # if self.object.login_required and not request.user.is_authenticated():
    #     #     pass
    #     if self.object.password and self.object.password != \
    #         self.request.session.get(self.session_key % self.object):
    #         return render_to_response('', {})

    #     response = super(self.__class__, self).get(request, *args, **kwargs)
