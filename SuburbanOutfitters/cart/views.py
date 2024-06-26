from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import CartItem, Order, Payment, ShippingAddress, Cart
from customer.models import Product, Customer
from .forms import CheckoutForm
from django.contrib.auth.models import User
from .models import CartItem
from django.contrib.auth.decorators import user_passes_test

class OrderDetailsView(DetailView):
    model = Order
    template_name = 'order_details.html'
    context_object_name = 'order'
    pk_url_kwarg = 'order_id'

class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders_list.html'
    queryset = Order.objects.all().order_by('-date_ordered')  # Order by most recent
@login_required
def cart_detail(request):
    # Retrieve the current user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()  # Fetch all cart items associated with the current user's cart
    return render(request, 'cart/cart_detail.html', {'cart': cart_items})

@login_required
def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart_detail')

@login_required
def cart_remove(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(user=request.user)
    CartItem.objects.filter(product=product, cart=cart).delete()
    return redirect('cart:cart_detail')

@login_required
def cart_edit(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if quantity:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        return redirect('cart:cart_detail')
    else:
        return render(request, 'cart/cart_edit.html', {'cart_item': cart_item})

@login_required
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
            return redirect('cart:checkout_complete')  # Redirect to a success page
    else:
        form = CheckoutForm()

    context = {
        'form': form
    }
    return render(request, 'cart/checkout.html', context)

@login_required
def checkout_complete(request):
    latest_order = Order.objects.latest('id')
    context = {
        'order_id': latest_order.id
    }
    return render(request, 'cart/checkout_complete.html', context)





