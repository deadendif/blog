# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20160520_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='is_spam',
            field=models.NullBooleanField(help_text=b'Whether email is spam.', verbose_name=b'is spam'),
        ),
        migrations.AlterField(
            model_name='email',
            name='success',
            field=models.NullBooleanField(default=False, help_text=b'Whether send email successfully.', verbose_name=b'success'),
        ),
    ]
