from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Products
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy


class FeedView(ListView):
    """Página Inicial, todos os produtos pela ordem mais recente"""
    model = Products 
    template_name = "products/feed.html"
    queryset = Products.objects.all().order_by('data_criacao')

class ProductView(DetailView):
    """Página de algum produto especifico"""
    model = Products
    template_name = "products/productDetail.html"
    context_object_name = 'product'

class NewProductView(LoginRequiredMixin, CreateView):
    """Formulário pra cadastrar um novo produto"""
    model = Products
    template_name = 'products/addProduct.html'
    form_class = ProductForm
    login_url = reverse_lazy('users:login')
    

    # Overriding form_valid to associate the user to the post
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateProductView(LoginRequiredMixin, UpdateView):
    """Atualizando informações cadastrais de produto"""
    model = Products
    template_name = 'products/addProduct.html'
    login_url = reverse_lazy('users:login')
    fields = ['name','info']
    

class DeleteProductView(LoginRequiredMixin, DeleteView):
    """Página de deletar produto"""
    model = Products
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('products:feed')



