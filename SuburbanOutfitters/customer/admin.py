from django.contrib import admin

# Register your models here.

from customer.models import Product,Customer

class ProductAdmin(admin.ModelAdmin):
    pass
class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product)
admin.site.register(Customer)