from django.db import models
from django.shortcuts import render
from django.urls import reverse

class Product(models.Model):
    GENDER_CHOICES = (
        ('M', 'Men'),
        ('W', 'Women'),
    )
    
    productName = models.CharField(max_length=200)
    productType = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    description = models.TextField(default='No description provided.')
    size = models.CharField(max_length=50, blank=True)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', default='default.jpg')

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'product_id': self.pk})

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/media/default.jpg"

    


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

