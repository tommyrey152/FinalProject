from django import forms

class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(label='Shipping Address', max_length=100)
    city = forms.CharField(label='City', max_length=50)
    card_number = forms.CharField(label='Card Number', max_length=16)
    expiration_date = forms.CharField(label='Expiration Date', max_length=7)
    cvv = forms.CharField(label='CVV', max_length=3)

