from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Products, Troca
from .forms import *

class FeedView(ListView):
	"""Front page, products ordered by most recent"""
	model = Products 
	template_name = "products/feed.html"
	context_object_name = 'products'
	paginate_by = 5
	queryset = Products.objects.all().order_by('created_at')	

	def get_queryset(self):
		user_query = self.request.GET.get('q')
		queryset = self.queryset

		if(user_query):
			description =  Q(info=user_query)
			name =  Q(name=user_query)
			username =  Q(user__username=user_query)

			queryset = queryset.filter(description | name | username)

		return queryset

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
    user_chosen= product_chosen.user
    saved = False

    if request.method == 'GET':
        form = ExchangeForm(initial={'product_chosen':product_chosen}, user=request.user)
        # Is the product mine?
        if product_chosen.user == request.user:
            raise PermissionDenied("Esse item é seu. Como você vai trocar consigo mesmo? O.o")
        # Have the product been exchanged?
        if not product_chosen.available:
            raise PermissionDenied("Desculpe, esse item já foi trocado. Quer tentar olhar outros")
        #  Is the product being exchanged?
        if Troca.objects.filter(Q(product_chosen=product_chosen) | Q(product_to_exchange=product_chosen)).exists():
            raise PermissionDenied("Desculpe, esse produto está em processo de troca, caso a troca não seja efetuada você pode tentar novamente")
    elif request.method == "POST":
        form = ExchangeForm(request.POST, initial={'product_chosen':product_chosen}, user=request.user)
        if form.is_valid():
            form.save()
            saved = True
    
    return render(
        request,
        'products/exchange.html',
        {
            'form': form, 
            'user': user_chosen, 
            'product_chosen': product_chosen, 
            'saved':saved
        }        
    )
