#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.core.mail import send_mail
from django.conf import settings

from lib.mixins import JSONResponseMixin
from about.forms import EmailForm

logger = logging.getLogger('file')


class AboutView(JSONResponseMixin, TemplateView):
    """
    About index view.
    """

    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        """
        Verifiy form and send email.
        """
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                ip = request.META.get('REMOTE_ADDR', '')
                ua = request.META.get('HTTP_USER_AGENT', '')
                email = form.save()
                email.ip = ip
                email.ua = ua
                email.save()
                send_mail(form.cleaned_data['topic'], form.cleaned_data['content'], settings.EMAIL_HOST_USER, [admin[1] for admin in settings.ADMINS])
            except Exception, e:
                logger.error(str(e))
                return self.response([{'status': 2, 'msg': 'System Error'}])
            else:
                return self.response([{'status': 0, 'msg': 'Success'}])
        else:
            return self.response([{'status': 3, 'msg': 'Invalid Form Data'}])
        