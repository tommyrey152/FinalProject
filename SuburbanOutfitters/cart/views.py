from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import CartItem
from customer.models import Product

def cart_detail(request):
    cart_items = CartItem.objects.all()
    return render(request, 'cart/cart_detail.html', {'cart': cart_items})

def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    product = Product.objects.get(id=product_id)
    CartItem.objects.filter(product=product).delete()
    return redirect('cart:cart_detail')

def checkout(request):
    if request.method == 'POST':
        # Process the checkout form data
        # This is where you would validate and save the form data to complete the checkout process
        return redirect('cart:checkout_complete')  # Redirect to a page indicating successful checkout
    else:
        # Display the checkout form
        return render(request, 'cart/checkout.html', {})