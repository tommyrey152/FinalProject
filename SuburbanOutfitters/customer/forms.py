from django import forms
from customer.models import Product
from .models import Customer
from django.contrib.auth.models import AbstractUser



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productName', 'productType', 'price', 'gender', 'description', 'size', 'quantity', 'image']


class CustomerCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('username', 'password', 'firstName', 'lastName', 'address')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
