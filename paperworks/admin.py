from django.contrib import admin

from .models import Sender,Recipient, Tag, Papermail

admin.site.register(Sender)
admin.site.register(Recipient)
admin.site.register(Tag)
admin.site.register(Papermail)