# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(help_text=b'Topic of the email.', max_length=128, verbose_name=b'email topic')),
                ('name', models.CharField(help_text=b'Name of the sender.', max_length=32, verbose_name=b'name')),
                ('address', models.EmailField(help_text=b'Email address of the sender.', max_length=254, verbose_name=b'address')),
                ('content', models.TextField(help_text=b'Email content.', verbose_name=b'content')),
                ('ip', models.GenericIPAddressField(help_text=b'IP of the sender.', null=True, verbose_name=b'IP', blank=True)),
                ('ua', models.CharField(help_text=b'User agent of the sender.', max_length=1024, null=True, verbose_name=b'user agent', blank=True)),
                ('send_time', models.DateTimeField(default=django.utils.timezone.now, help_text=b'Datetime when sending email.', verbose_name=b'email time')),
                ('success', models.BooleanField(default=False, help_text=b'Whether send email successfully.', verbose_name=b'success')),
            ],
        ),
    ]
