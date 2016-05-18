# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='name',
            field=models.CharField(help_text=b'Name of the sender.', max_length=32, verbose_name=b'name'),
        ),
        migrations.AlterField(
            model_name='email',
            name='topic',
            field=models.CharField(help_text=b'Topic of the email.', max_length=128, verbose_name=b'email topic'),
        ),
        migrations.AlterField(
            model_name='email',
            name='ua',
            field=models.CharField(help_text=b'User agent of the sender.', max_length=1024, null=True, verbose_name=b'user agent', blank=True),
        ),
    ]
