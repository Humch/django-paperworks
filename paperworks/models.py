from django.db import models
from django.db.models import signals
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.utils.deconstruct import deconstructible
from django.conf import settings

from wand.image import Image

import os
from uuid import uuid4

paperworks_media_root = getattr(settings, 'PAPERWORKS_MEDIA_ROOT','')

class Sender(models.Model):
    
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('papermail-list')

class Recipient(models.Model):
    
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('papermail-list')

class Tag(models.Model):
    
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

@deconstructible
class PathAndRename(object):

    """Rename the file with uuid64 module"""

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
         # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
            return os.path.join(self.path, filename)
        return wrapper

path_and_rename = PathAndRename(paperworks_media_root)

class Papermail(models.Model):
    
    paper_file = models.FileField(upload_to = path_and_rename)
    name_file = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to = paperworks_media_root, blank=True)
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag,blank=True)
    date_creation = models.DateTimeField(auto_now_add = True)
    date_modification = models.DateTimeField(auto_now = True)
    date_paper = models.DateField()
    property_of = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paperwork_owner')
    shared_with = models.ManyToManyField(User, blank=True, related_name='paperwork_user')

    def __str__(self):
        return self.name_file
    
    def get_absolute_url(self):
        return reverse('papermail-detail', kwargs={'pk': self.pk})