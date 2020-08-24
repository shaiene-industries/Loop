from django import forms
from .models import Post
from markdownx.fields import MarkdownxFormField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","author", "body",)
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body': MarkdownxFormField(),
        }

        labels = {
            'title': ('Title*'),
            'author': ('Author*'),
        }
        
