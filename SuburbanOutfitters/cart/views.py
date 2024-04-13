from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import CartItem, Order, Payment, ShippingAddress
from customer.models import Product, Customer
from .forms import CheckoutForm



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
            # Retrieve the current customer
            customer = Customer.objects.get(id=request.user.id)
            shipping_address = ShippingAddress.objects.create(
                customer=customer,
                address=customer.address,
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                zipcode=form.cleaned_data['zipcode']
            )
            order = Order.objects.create(
                # Your other fields
                shipping_address=shipping_address
            )
            return redirect('checkout_complete')  # Redirect to a success page
    else:
        form = CheckoutForm()

    context = {
        'form': form
    }
    return render(request, 'cart/checkout.html', context)


def checkout_complete(request):
    print("Redirecting to checkout_complete")
    return render(request, 'cart/checkout_complete.html')