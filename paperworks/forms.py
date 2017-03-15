from django import forms
from django.forms import ModelForm, FileInput, FileField, Select, ModelChoiceField, DateField, CharField, ModelMultipleChoiceField
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

from .models import Papermail, Tag, Sender, Recipient

class SenderForm(ModelForm):
    """
    Model form to create Sender Model object
    """
    
    name = CharField(
                label = _("Name")
    )
    
    class Meta:
        
        model = Sender
        fields = ['name']

class RecipientForm(ModelForm):
    """
    Model form to create Recipient Model object
    """
    
    name = CharField(
                label = _("Name")
    )
    
    class Meta:
        
        model = Recipient
        fields = ['name']

class PapermailForm(ModelForm):
    """
    Model form to create and update Papermail Model object
    """
    
    paper_file = FileField(
                    label = _("File"),
                    required=False,
                    widget = FileInput()
                )
    
    name_file = CharField(
                    label = _("Papermail")
    )
    
    sender = ModelChoiceField(
                queryset = Sender.objects.all(),
                label = mark_safe(_("Sender") + ' <a href="#" onClick="addSender()"><i class="fi-plus green-color"></i></a>'),
                widget = Select(attrs={'required':True})
            )
    
    recipient = ModelChoiceField(
                queryset = Recipient.objects.all(),
                label = mark_safe(_("Recipient") + ' <a href="#" onClick="addRecipient()"><i class="fi-plus green-color"></i></a>'),
                widget = Select(attrs={'required':True})
            )
    
    date_paper = DateField(
                    label = _("Papermail's Date")
    )
    
    tag = ModelMultipleChoiceField(
                queryset = Tag.objects.all(),
                label = _("Tags")
    )

    class Meta:
        
        model = Papermail
        fields = ['paper_file','name_file','sender','recipient','date_paper','tag']
        

        