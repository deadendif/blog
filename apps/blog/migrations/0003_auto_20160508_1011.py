# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_site'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_caption',
            new_name='caption',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(help_text=b'Used in entry.', upload_to=b'', verbose_name=b'image', blank=True),
        ),
    ]
