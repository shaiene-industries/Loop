from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index/index.html',{})
    
def base(request):
    return render(request,'base/base.html',{})    