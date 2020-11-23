from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Products
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy


def home(request):
    return render(request,'products/index.html',{})
    
def base(request):
    return render(request,'base/base.html',{})  

class FeedView(ListView):
    model = Products 
    template_name = "products/feed.html"

class ProductView(DetailView):
    model = Products
    template_name = "products/productDetail.html"
    context_object_name = 'product'

class NewProductView(LoginRequiredMixin, CreateView):
    model = Products
    template_name = 'products/addProduct.html'
    form_class = ProductForm
    login_url = reverse_lazy('users:login')
    

    # Overriding form_valid to associate the user to the post
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateProductView(LoginRequiredMixin, UpdateView):
    model = Products
    template_name = 'products/addProduct.html'
    login_url = reverse_lazy('users:login')
    fields = ['name','info']
    

class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Products
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('products:feed')



#Function Views
# def base(request):
#     return render(request,'base/base.html',{})

# def home(request):
#     return render(request,'home.html', {})
