# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='weight',
            field=models.IntegerField(default=0, help_text=b'Used to sort category.', verbose_name=b'weight'),
        ),
    ]
