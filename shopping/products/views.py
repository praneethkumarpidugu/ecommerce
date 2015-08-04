from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    if request.user.is_authenticated():
        #sample = "Praneeth Kumar Pidugu"
        context = {"sample":request.user}
    else:
        context = {"sample": request.user}
    template = 'products/home.html'
    return render(request, template, context)

def all(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'

    return render(request, template, context)