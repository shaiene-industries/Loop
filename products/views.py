from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Products
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy


class FeedView(ListView):
    """Front page, products ordered by most recent"""
    model = Products 
    template_name = "products/feed.html"
    context_object_name = 'products'
    paginate_by = 2
    queryset = Products.objects.all().order_by('created_at')

class ProductView(DetailView):
    """Product detail page"""
    model = Products
    template_name = "products/productDetail.html"
    context_object_name = 'product'

class NewProductView(LoginRequiredMixin, CreateView):
    """Form to add new products"""
    model = Products
    template_name = 'products/addProduct.html'
    form_class = ProductForm
    login_url = reverse_lazy('users:login')
    

    # Overriding form_valid to associate the user to the post
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateProductView(LoginRequiredMixin, UpdateView):
    """Updating product information"""
    model = Products
    template_name = 'products/addProduct.html'
    login_url = reverse_lazy('users:login')
    fields = ['name','info']
    

class DeleteProductView(LoginRequiredMixin, DeleteView):
    """Página de deletar produto"""
    """Delete a product"""
    model = Products
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('products:feed')



