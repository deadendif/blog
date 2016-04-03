#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import View

from blog.mixins.json_response import JSONResponseMixin

class TestView(JSONResponseMixin, View):

    def get(self, request):
        print 'xxx'
        return self.render_to_response("123321123321")