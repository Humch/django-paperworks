from django.db import models
from django.db.models import signals
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.conf import settings

from wand.image import Image

paperworks_media_root = getattr(settings, 'PAPERWORKS_MEDIA_ROOT')
paperworks_media_thumb_default = getattr(settings, 'PAPERWORKS_MEDIA_THUMB_DEFAULT','static/paperworks/images/default_thumb.jpg')

class Sender(models.Model):
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Recipient(models.Model):
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Papermail(models.Model):
    
    paper_file = models.FileField(upload_to=paperworks_media_root)
    name_file = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to=paperworks_media_root,default=paperworks_media_thumb_default,blank=True)
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
        return reverse('name-file-detail', kwargs={'pk': self.pk})
    
# TODO ==> creer une methode post_save