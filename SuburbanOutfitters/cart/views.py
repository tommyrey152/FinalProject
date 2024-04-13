from django.shortcuts import render, redirect
from .models import CartItem, Order, Payment, ShippingAddress
from customer.models import Product
from .forms import CheckoutForm
from .models import Cart

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
            shipping_address = ShippingAddress.objects.create(
                street_address=form.cleaned_data['shipping_address'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                zipcode=form.cleaned_data.get('zipcode', '')  # Use get method with a default value
            )
            payment = Payment.objects.create(
                card_number=form.cleaned_data['card_number'],
                expiration_date=form.cleaned_data['expiration_date'],
                cvv=form.cleaned_data['cvv']
            )
            order = Order.objects.create(
                shipping_address=shipping_address,
                payment=payment
            )
            return render(request, 'cart/checkout_complete.html', {'order': order})
    else:
        form = CheckoutForm()
    return render(request, 'cart/checkout.html', {'form': form})



def checkout_complete(request):
    # Add any logic here for the checkout completion
    return render(request, 'cart/checkout_complete.html')
