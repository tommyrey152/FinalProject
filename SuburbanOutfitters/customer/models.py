from django.db import models
from django.shortcuts import render
from django.urls import reverse

class Product(models.Model):
    productName = models.CharField(max_length=200)
    productType = models.CharField(max_length=200)
    

class Customer(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.firstName
    

def mens_products(request):
    # Your logic here
    return render(request, 'mens_products.html')

def womens_products(request):
    # Your logic here
    return render(request, 'womens_products.html')

def all_products(request):
    # Your logic here
    return render(request, 'all_products.html')


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])

