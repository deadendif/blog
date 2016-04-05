#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import View

from mixins.json_response import JSONResponseMixin, RenderMixin

# class TestJsonView(JSONResponseMixin, View):

#     def get(self, request):
#         print 'xxx'
#         return self.render_to_response("123321123321")

class TestView(RenderMixin, View):

    def get(self, request):
        return self.render_to_response('blog/index.html')
