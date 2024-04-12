from django import forms
from customer.models import Product, ProductSize
from .models import Customer

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productName', 'productType', 'price', 'gender', 'description', 'image']

        
class ProductSizeForm(forms.ModelForm):
    class Meta:
        model = ProductSize
        fields = ['size', 'quantity']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)