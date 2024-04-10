from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=200)
    productType = models.CharField(max_length=200)




