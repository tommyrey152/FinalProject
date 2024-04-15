from django import forms
from customer.models import Product
from .models import Customer, MarketingCampaign, Profile
from django.contrib.auth.models import AbstractUser
from .models import CostReport



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productName', 'productType', 'price', 'gender', 'description', 'size', 'quantity', 'image']


class CustomerCreationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('firstName', 'lastName', 'address')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    

class MarketingCampaignForm(forms.ModelForm):
    class Meta:
        model = MarketingCampaign
        fields = '__all__'   

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'address', 'phone_number', 'email']




class CostReportForm(forms.ModelForm):
    class Meta:
        model = CostReport
        fields = ['name', 'cost', 'description']