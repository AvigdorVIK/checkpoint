from django import forms
from .models import *

class AddForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['title', 'content']

