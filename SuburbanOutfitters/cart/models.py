from django.db import models
from customer.models import Product, Customer, ShippingAddress
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='shipping_addresses')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.address}, {self.city}, {self.state} {self.zipcode}'

class Payment(models.Model):
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=7)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return f"Payment: {self.card_number}, {self.expiration_date}, {self.cvv}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    payment = models.ForeignKey('cart.Payment', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f"Order {self.id}"
    
    def get_total_price(self):
        total = sum(item.product.price * item.quantity for item in self.items.all())  # Use 'items' instead of 'cartitem_set'
        return total
