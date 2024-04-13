from django.shortcuts import render, redirect
from .models import CartItem
from customer.models import Product
from .forms import CheckoutForm
from .models import Order

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
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process the form data
            shipping_address = form.cleaned_data['shipping_address']
            city = form.cleaned_data['city']
            card_number = form.cleaned_data['card_number']
            expiration_date = form.cleaned_data['expiration_date']
            cvv = form.cleaned_data['cvv']
            # Redirect to a success page or do something else
            return redirect('cart:checkout_complete')
    else:
        form = CheckoutForm()
    
    return render(request, 'cart/checkout.html', {'form': form})


def checkout_complete(request):
    # Add any logic here for the checkout completion
    return render(request, 'cart/checkout_complete.html')
