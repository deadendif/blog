# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models.image
import tagging.fields
import mptt.fields
import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Title of the category.', max_length=255, verbose_name=b'title')),
                ('slug', models.SlugField(help_text=b"Used to build the category' URL.", unique=True, max_length=255, verbose_name=b'slug')),
                ('description', models.TextField(help_text=b'Describe the category.', verbose_name=b'description', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='blog.Category', help_text=b'Parent category.', null=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Title of the entry.', max_length=255, verbose_name=b'title')),
                ('slug', models.SlugField(help_text=b"Used to build the entry' URL.", max_length=255, verbose_name=b'slug')),
                ('status', models.IntegerField(default=1, help_text=b'Status of the entry.', db_index=True, verbose_name=b'status', choices=[(1, b'draft'), (2, b'hidden'), (3, b'published')])),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text=b'Datetime when create the entry.', verbose_name=b'Create time', db_index=True)),
                ('start_publish', models.DateTimeField(help_text=b'Datetime when starting publication', null=True, verbose_name=b'start publish', db_index=True, blank=True)),
                ('end_publish', models.DateTimeField(help_text=b'Datetime when stopping publication', null=True, verbose_name=b'end publish', db_index=True, blank=True)),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now, help_text=b'Datetime when last update the entry.', verbose_name=b'last update time')),
                ('excerpt', models.TextField(help_text=b'Used to SEO purposes.', verbose_name=b'excerpt', blank=True)),
                ('content', models.TextField(help_text=b'Content of the entry.', verbose_name=b'content', blank=True)),
                ('featured', models.BooleanField(default=False, help_text=b'Telling if the entry is featured', verbose_name=b'featrue')),
                ('tags', tagging.fields.TagField(max_length=255, verbose_name=b'tags', blank=True)),
                ('login_required', models.BooleanField(default=False, help_text=b'Telling if user need to be authenticated.', verbose_name=b'login required')),
                ('password', models.CharField(help_text=b'Protects the entry with a password.', max_length=64, verbose_name=b'password', blank=True)),
                ('detail_template', models.CharField(default=(b'xxx', b'111'), help_text=b'The detail tempate of the entry.', max_length=255, verbose_name=b'detail template', choices=[(b'xxx', b'111')])),
                ('author', models.ForeignKey(related_name='entries', on_delete=django.db.models.deletion.SET_NULL, to='blog.Author', help_text=b'Author of the entry.', null=True)),
                ('categories', models.ManyToManyField(help_text=b'Categories that contain this entry.', related_name='entries', to='blog.Category', blank=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'get_latest_by': 'creation_date',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_caption', models.TextField(help_text=b"Image' caption.", verbose_name=b'image caption', blank=True)),
                ('image', models.ImageField(help_text=b'Used in entry.', upload_to=blog.models.image.upload_image_to, verbose_name=b'image', blank=True)),
                ('entry', models.ForeignKey(related_name='images', to='blog.Entry', help_text=b'Entry that contains this image.')),
            ],
        ),
    ]
