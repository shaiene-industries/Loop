from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import LoginForm
#from django.auth.
# Create your views here.


# Using generic view, CreateView. The fields var, sets which attributes of User will be required 
# This functionality is made using django's default create functionality
class CreateUser(CreateView):
    template_name = 'users/create.html'
    model = User
    fields = ['username', 'email', 'password']

# The login function view, tries to login when the request method is POST 
# and redirects to a login page when it is GET 
# This functionality is kind of "manual", as there is a django functionality that does login automatically
def loginUser(request):   
    if request.method == 'POST':
        # Validating form, 
        form = LoginForm(request.POST)
        # Validating form and logging in if it is valid
        if form.is_valid():
            print("Form is valid")
            name = form.cleaned_data.get('username')
            passwd = form.cleaned_data.get('password')
            user = authenticate(username=name, password=passwd)
            login(request, user)
            print("Login Successful")
            redirect('posts')
        print("Form is not valid")
    else:
        # Redirecting to login page using Login Form
        form = LoginForm()
    return render(request,'users/login.html', {'form':form})
        


