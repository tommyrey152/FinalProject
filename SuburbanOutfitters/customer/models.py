from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=200)
    productType = models.CharField(max_length=200)

class Customer(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.firstName


