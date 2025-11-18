from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from .cart import Cart

def cart_add(request, product_id):
    cart = Cart(request) # Grab the basket
    product = get_object_or_404(Product, id=product_id) # Find the product
    cart.add(product=product) # Put it in the basket
    return redirect('cart:cart_detail') # Go to the cart page

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})