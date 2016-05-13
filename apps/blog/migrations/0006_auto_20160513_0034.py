# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160513_0016'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryCounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_view_num', models.IntegerField(default=0, help_text=b'The page view number of the entry.', verbose_name=b'page view number')),
                ('useful_num', models.IntegerField(default=0, help_text=b'The number of people who thinks the entry is useful.', verbose_name=b'useful number')),
                ('useless_num', models.IntegerField(default=0, help_text=b'The number of people who thinks the entry is useful.', verbose_name=b'useful number')),
            ],
        ),
        migrations.RemoveField(
            model_name='entry',
            name='page_view_num',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='useful_num',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='useless_num',
        ),
    ]
