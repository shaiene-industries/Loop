from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Products, Troca
from django.contrib.auth.decorators import login_required
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
    """Delete a product"""
    model = Products
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('products:feed')

@login_required
def exchange(request,pk):
    """
    Receives an Product primary key and resolves if that product is aceptable to be exchanged, if yes, display exchange 
    page with exchange form. Also saves form.
    """
    product_chosen = get_object_or_404(Products,pk=pk) 

    if request.method == 'GET':
        # Is the product mine?
        if product_chosen.user == request.user:
            raise PermissionDenied("Esse item é seu. Como você vai trocar consigo mesmo? O.o")
        # Have the product been exchanged?
        if not product_chosen.available:
            raise PermissionDenied("Desculpe, esse item já foi trocado. Quer tentar olhar outros")
        #  Is the product being exchanged?
        if Troca.objects.filter(Q(product_chosen=product_chosen) | Q(product_to_exchange=product_chosen)).exists():
            raise PermissionDenied("Desculpe, esse produto está em processo de troca, caso ele a troca não seja efetuada você pode tentar novamente")
    elif request.method == "POST":
        form = ExchangeForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = ExchangeForm(product_chosen=product_chosen, user=request.user)
    user_product = product_chosen.user

        
    return render(
        request,
        'products/exchange.html',
        {
            'form': form, 
            'user': user_product, 
            'product': product_chosen, 
        }        
    )



# Esse item é seu. Como você vai trocar consigo mesmo? O.o
# Desculpe, esse item já foi trocado. Quer tentar olhar outros
