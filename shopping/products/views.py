from django.shortcuts import render, Http404
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    template = 'products/home.html'
    context = {"products": products}
    return render(request, template, context)

def all(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'

    return render(request, template, context)

def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        products = Product.objects.all()
        context = {'product': product}
        template = 'products/single.html'
    except:
        raise Http404

    return render(request, template, context)