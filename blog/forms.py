from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","author", "body")

        
