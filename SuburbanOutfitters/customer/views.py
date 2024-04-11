from django.shortcuts import render
from django.views import View
from .models import Product,Customer

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'product_list.html', context=context)

class CustomerList(View):
    def get(self,request):
        customers = Customer.objects.all()
        return render(request = request,template_name = 'customer_list.html',context = {'customers':customers})