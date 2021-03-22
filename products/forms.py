from itertools import chain
from django import forms
from django.forms import widgets
from django.forms.models import inlineformset_factory
from django.forms.widgets import HiddenInput
from .models import *
from markdownx.fields import MarkdownxFormField
from utils.form_utils import bootstrap_format
from django_select2.forms import ModelSelect2MultipleWidget, Select2Widget

class ProductForm(forms.ModelForm):
    info = MarkdownxFormField()
    class Meta:
        model = Products
        fields = ("name", "category", "info", "trocopor")

        widgets = {
            'trocopor': ModelSelect2MultipleWidget(
                model = Products,
                search_fields=['name__icontains','category__icontains']
            )
        }

        labels = {
            "name": "Nome",
            "category": "Categoria",
        }

    def __init__(self,*args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['info'].label = "Descrição"
        self.fields = bootstrap_format(self.fields,float=True)
        self.fields['info'].widget.attrs["resize"]= "none"
        self.fields['info'].widget.attrs["placeholder"]= "Descreva aqui, da maneira que quiser, informações sobre seu item.\
            Caso queira deixar seu texto em negrito coloque ele entre **dois pares astericos**.\
            Caso queira deixa-lo em itálico coloque entre *um par de asteriscos*.\
            Para criar titulos coloque # no inicio da linha separado do texto, para subtitulos use duas ##\
            Para textos ainda menores pode usar ### e assim em diante."

class Product_ImageForm(forms.ModelForm):
    class Meta:
        model = Product_Image
        fields = ("image",)

        labels = {
            "image":""
        }


ProductInlineFormSet = inlineformset_factory(Products, Product_Image,form=Product_ImageForm,)


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

    # def save(self, commit=True):


    

