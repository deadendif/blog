# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160518_1510'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email',
        ),
    ]
