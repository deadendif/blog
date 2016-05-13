# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160512_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='page_views',
            new_name='page_view_num',
        ),
        migrations.AddField(
            model_name='entry',
            name='useful_num',
            field=models.IntegerField(default=0, help_text=b'The number of people who thinks the entry is useful.', verbose_name=b'useful number'),
        ),
        migrations.AddField(
            model_name='entry',
            name='useless_num',
            field=models.IntegerField(default=0, help_text=b'The number of people who thinks the entry is useful.', verbose_name=b'useful number'),
        ),
    ]
