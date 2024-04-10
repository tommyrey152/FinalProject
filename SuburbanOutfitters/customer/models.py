from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=200)
    productType = models.CharField(max_length=200)
    










# class tShirt(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     color = models.CharField(max_length=100)
#     size = models.CharField(max_length=100)
#     brand = models.CharField(max_length=100)

# class Pants(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     color = models.CharField(max_length=100)
#     size = models.CharField(max_length=100)
#     brand = models.CharField(max_length=100)
    
# class Shorts(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     color = models.CharField(max_length=100)
#     size = models.CharField(max_length=100)
#     brand = models.CharField(max_length=100)

# class sweatShirt(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     color = models.CharField(max_length=100)
#     size = models.CharField(max_length=100)
#     brand = models.CharField(max_length=100)

# class Hats(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     color = models.CharField(max_length=100)
#     size = models.CharField(max_length=100)
#     brand = models.CharField(max_length=100)

