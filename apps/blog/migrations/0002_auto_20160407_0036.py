# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='categories',
        ),
        migrations.AddField(
            model_name='entry',
            name='category',
            field=models.ForeignKey(related_name='entries', to='blog.Category', help_text=b'Categories that contain this entry.', null=True),
        ),
    ]
