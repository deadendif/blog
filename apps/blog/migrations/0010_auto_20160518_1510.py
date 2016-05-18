# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160518_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='ip',
            field=models.GenericIPAddressField(help_text=b'IP of the sender.', null=True, verbose_name=b'IP', blank=True),
        ),
    ]
