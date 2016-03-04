
import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import get_user_model
from deadend.setting import DRAFT, HIDDEN, PUBLISHED
from deadend.setting import ENTRY_DETAIL_TEMPLATES, UPLOAD_IMAGE_TO

class Author(get_usre_model()):
    pass

class Entry(models.Model):
    """
    Entry model class
    """
    STATUS = (
        (DRAFT, 'draft'),
        (HIDDEN, 'hidden'),
        (PUBLISHED, 'published')
    )

    title = models.CharField('title', 
            max_length=255,
            help_text='Title of the entry.')
    slug = models.SlugField('slug', 
            max_length=255,
            help_text='Used to build the entry\' URL.')
    status = models.IntegerField('status', 
            db_index=True, choice=STATUS, default=DRAFT,
            help_text='Status of the entry.')
    create_time = models.DateTimeField('Create time',
            db_index=True, default=timezone.now,
            help_text='Datetime when create the entry.')
    start_publish = models.DateTimeField('start publish',
            db_index=True, blank=True, null=True,
            help_text='Datetime when starting publication')
    end_publish = models.DateTimeField('end publish',
            db_index=True, blank=True, null=True,
            help_text='Datetime when stopping publication')
    last_update = models.DateTimeField('last update time',
            default=timezone.now,
            help_text='Datetime when last update the entry.')
    lead = models.TextField('lead',
            blank=True,
            help_text='Lead paragraph of the entry.')
    excerpt = models.TextField('excerpt',
            blank=True,
            help_text='Used to SEO purposes.')
    content = models.TextField('content',
            blank=True,
            help_text='Content of the entry.')
    featured = models.BooleanField('featrue',
            default=False,
            help_text='Telling if the entry is featured')
    author = models.ForeignKey(
            Author, related_name='entries', on_delete=models.SET_NULL,  # ???
            help_text='Author of the entry.')
    categories = models.ManyToManyField(
            Category, related_name='categories', blank=True,
            help_text='Categories that contain this entry.')
    tags = TagField('tags')
    login_required = models.BooleanField('login required',
            default=False,
            help_text='Telling if user need to be authenticated.')
    password = models.CharField('password',
            max_length=64, blank=True,
            help_text='Protects the entry with a password.')
    detail_template = models.CharField('detail template',
            max_length=255, choices=ENTRY_DETAIL_TEMPLATES,
            default=ENTRY_DETAIL_TEMPLATES[0],
            help_text='The detail tempate of the entry.')

    class Meta:
        ordering = ['-create_time']
        get_latest_by = 'creation_date'


def upload_image_to(filename):
    now = timezone.now()
    filename, extension = os.path.splitext(filename)
    path = os.path.join(UPLOAD_IMAGE_TO, now.strftime('%Y/%m/%d'), 
            '%s.%s' % (str(uuid.uuid4()), extension))
    return path


class Image(models.Model):
    """
    Image in entry
    """
    image_caption = models.TextField('image caption',
            blank=True,
            help_text='Image\' caption.')
    image = models.ImageField('image',
            blank=True, upload_to=upload_image_to,
            help_text='Used in entry.')
    entry = models.ForeignKey(
            Entry, related_name='images',
            help_text='Entry that contains this image.')


class Category(models.Model):
    """
    Entry's Category
    """


