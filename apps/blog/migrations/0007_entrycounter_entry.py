# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160513_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrycounter',
            name='entry',
            field=models.OneToOneField(related_name='counter', null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Entry', help_text=b'The entry that counter belongs to.'),
        ),
    ]
