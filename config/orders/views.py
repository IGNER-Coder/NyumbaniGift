from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        # If the user hit the "Place Order" button
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # 1. Save the Order info (Name, address, etc.)
            order = form.save()
            
            # 2. Loop through the cart and save each item
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            
            # 3. Clear the cart
            cart.clear()
            
            # 4. Show the success page
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        # If the user just arrived at the page
        form = OrderCreateForm()
        
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})