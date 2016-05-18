#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from about.models import Email


class EmailForm(forms.ModelForm):
    """
    Email form.
    """

    class Meta:
        model = Email
        fields = ['topic', 'name', 'address', 'content', 'ip', 'ua']