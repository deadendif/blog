# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='is_spam',
            field=models.BooleanField(default=True, help_text=b'Whether email is spam.', verbose_name=b'is spam'),
        ),
        migrations.AlterField(
            model_name='email',
            name='ip',
            field=models.CharField(help_text=b'IP of the sender.', max_length=64, null=True, verbose_name=b'IP', blank=True),
        ),
    ]
