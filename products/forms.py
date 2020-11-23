from django import forms
from .models import Products
from markdownx.fields import MarkdownxFormField

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ("name", "category","info")
        
        widgets = {
            'body': MarkdownxFormField(),
        }

        
