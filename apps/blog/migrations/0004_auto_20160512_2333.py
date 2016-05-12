# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models.image


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160508_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='page_views',
            field=models.IntegerField(default=0, help_text=b'The page view number of the entry.', verbose_name=b'page view number'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(help_text=b'Used in entry.', upload_to=blog.models.image.upload_image_to, verbose_name=b'image', blank=True),
        ),
    ]
