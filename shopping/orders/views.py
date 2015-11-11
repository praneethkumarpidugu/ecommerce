import time
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect
from carts.models import Cart
from .models import Order
from .utils import id_generator
# Create your views here.

def orders(request):
    context = {}
    template = "orders/user.html"
    return render(request, template, context)

#require user login **
def checkout(request):

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
        print(cart)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))

    new_order, created = Order.objects.get_or_create(cart=cart)
    if created:
        #assign a user to the order
        #assign address
        new_order.order_id = str(time.time())
        new_order.save()
    new_order.user = request.user
    new_order.save()
    #run credit card
    if new_order.status == "Finished":
        #cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("cart"))

    context = {}
    template = "products/home.html"
    return render(request, template, context)