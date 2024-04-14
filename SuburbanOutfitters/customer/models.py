from django.db import models
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User


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

    def __str__(self):
        return self.productName

class Customer(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128, null=True)
    last_login = models.DateTimeField(auto_now=True)

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
        return reverse('category_detail', args=[str(self.id)]);
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.address}, {self.city}, {self.state} {self.zipcode}'
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

   

# Extend the User model with a one-to-one relationship
User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
    
    
class MarketingCampaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discountPercent = models.CharField(max_length=255)
    startDate = models.DateField()
    endDate = models.DateField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
  
#sales Report 
class Sale(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

class Cost(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()