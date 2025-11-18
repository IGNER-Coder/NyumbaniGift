from django.shortcuts import render, get_object_or_404 # Import this!
from .models import Product

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/index.html', context)

# Add this new function
def product_detail(request, slug):
    # Try to get the product with this slug. If not found, show 404 error.
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'store/product_detail.html', context)

def about(request):
    return render(request, 'store/about.html')