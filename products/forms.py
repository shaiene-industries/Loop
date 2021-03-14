from itertools import chain
from django import forms
from django.forms.widgets import HiddenInput
from .models import Products, Troca
from markdownx.fields import MarkdownxFormField
from utils.form_utils import *
from django_select2.forms import Select2Widget, Select2TagWidget

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ("name", "category", "info")
        
        widgets = {
            'body': MarkdownxFormField(),
        }

        labels = {
            "name": "Nome",
            "category": "Categoria",
            "info": u"Descrição",
        }


class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Troca
        fields = ("product_chosen","product_to_exchange")

        widgets = {
            "product_to_exchange": Select2Widget,
            "product_chosen": HiddenInput
        }
        
        labels = {
            "product_to_exchange": u"Escolha um item seu:",
        }

    def __init__(self,*args, **kwargs):
        user = kwargs.pop('user',False) 
        super(ExchangeForm, self).__init__(*args, **kwargs)
        if user:
            troco_cat = [ troco.get('category') for troco in self.initial['product_chosen'].trocopor.values('category').distinct() ]
            self.fields['product_to_exchange'].queryset = Products.objects.filter(user=user,category__in=troco_cat)

    def clean(self):
        cleaned_data =  super(ExchangeForm, self).clean()
        cleaned_data['product_chosen'] = self.initial['product_chosen']
        return cleaned_data

    

