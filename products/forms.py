from django import forms
from django.forms.widgets import HiddenInput
from .models import Products, Troca
from markdownx.fields import MarkdownxFormField
from utils.form_utils import *
from django_select2.forms import Select2Widget

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
        product_chosen = kwargs.pop('product_chosen',False) 
        user = kwargs.pop('user',False) 
        super().__init__(*args, **kwargs)
        if product_chosen:
            self.fields['product_chosen'].initial = product_chosen
        if user:
            troco_cat = [ troco.get('category') for troco in product_chosen.trocopor.values('category').distinct() ]
            self.fields['product_to_exchange'].queryset = Products.objects.filter(user=user,category__in=troco_cat)

    def clean(self):
        data =  super().clean()
        print("uh lala")
    
    def save(self, commit=True):
        troca = super(ExchangeForm, self).save(commit=commit)
        if 'product_chosen' in self.changed_data:
            self.fields[]
        return troca

    

