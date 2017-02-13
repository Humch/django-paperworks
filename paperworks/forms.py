from django.forms import ModelForm, FileInput, FileField, Select, ModelChoiceField, DateField

from django import forms

from django.utils.safestring import mark_safe

from .models import Papermail, Tag, Sender, Recipient

class PapermailForm(ModelForm):
    """
    Model form to create and update Papermail Model object
    """
    
    paper_file = FileField(
                    required=False,
                    widget = FileInput()
                )
    
    sender = ModelChoiceField(
                queryset = Sender.objects.all(),
                label = mark_safe('Sender <a href="#" onClick="addSender()"><i class="fi-plus green-color"></i></a>'),
                widget = Select(attrs={'required':True})
            )
    
    recipient = ModelChoiceField(
                queryset = Recipient.objects.all(),
                label = mark_safe('Recipient <a href="#" onClick="addRecipient()"><i class="fi-plus green-color"></i></a>'),
                widget = Select(attrs={'required':True})
            )

    class Meta:
        
        model = Papermail
        fields = ['paper_file','name_file','sender','recipient','date_paper','tag']
        

        