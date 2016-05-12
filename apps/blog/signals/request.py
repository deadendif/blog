#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.zlovezl.cn/articles/implement-an-efficient-counter-in-django/
# http://www.zlovezl.cn/?page=2

from django.core.signals import request_started, request_finished
from django.dispatch import receiver

@receiver(request_finished)
def increase_page_view(sender, **kwargs):
    """
    Increase page view number when accessed.
    """
    pass
