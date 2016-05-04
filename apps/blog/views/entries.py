#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.dates import BaseDateDetailView

from mixins.entries import EntryDetailMixin


class EntryDetail(EntryDetailMixin, BaseDateDetailView):
    """
    Entry detail view.
    TODO: entry login and password protections.
    """
    # session_key = 'entry_passwd_%s'

    def get_context_data(self, **kwargs):
        context = super(EntryDetail, self).get_context_data(**kwargs)
        return context

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
