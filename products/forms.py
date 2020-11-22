from django import forms
from .models import Products
from markdownx.fields import MarkdownxFormField

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ("title", "body",)
        
#         widgets = {
#             'title':forms.TextInput(attrs={'class':'form-control'}),
#             'body': MarkdownxFormField(),
#         }

#         labels = {
#             'title': ('Title'),
#         }
        
