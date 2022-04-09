from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    class Meta:
        model= Search
        fields= '__all__'

