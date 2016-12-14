from django.forms import ModelForm, FileInput, FileField
from django import forms

from .models import Papermail, Tag, Sender

class PapermailUpdateForm(ModelForm):
    
    paper_file = forms.FileField(
                    required=False,
                    widget = FileInput()
                )
    
    class Meta:
        
        model = Papermail
        fields = ['paper_file','name_file','sender','recipient','date_paper','tag']

        