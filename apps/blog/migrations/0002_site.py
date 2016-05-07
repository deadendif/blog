# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Title of the site.', max_length=255, verbose_name=b'title')),
                ('url', models.URLField(help_text=b'URL of the site.', max_length=255, verbose_name=b'URL')),
                ('added_time', models.DateTimeField(default=django.utils.timezone.now, help_text=b'Datetime when the site is added', verbose_name=b'Added time')),
                ('is_visible', models.BooleanField(default=True, help_text=b'Whether the site is visible.', verbose_name=b'Visibility')),
            ],
        ),
    ]
