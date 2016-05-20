# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20160520_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='success',
            field=models.BooleanField(default=False, help_text=b'Whether send email successfully.', verbose_name=b'success'),
        ),
    ]
