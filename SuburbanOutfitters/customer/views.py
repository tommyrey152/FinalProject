from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product,Customer
from .forms import ProductForm
from django.urls import reverse
from .forms import CustomerForm



class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'product_list.html', context=context)

class CustomerList(View):
    def get(self,request):
        customers = Customer.objects.all
        return render(request = request,template_name = 'customer_list.html',context = {'customers':customers})
    

class ProductAdd(View):

    def get(self,request):
        form = ProductForm()
        return render(request = request,template_name = 'product_add.html',context = {'form':form})
    
    def post(self,request):
        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.save()
        
        return render(request = request,template_name = 'product_add.html',context = {'product':product,'form':form})
    

class ProductDetails(View):

    def get(self,request,product_id=None):

        if product_id:
            product = Product.objects.get(pk=product_id)
        else:
            product = Product()

        form = ProductForm(instance=product)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'product_details.html',context = {'product':product,'form':form})
    
    def post(self,request,product_id=None):
        return redirect(reverse("product_list"))
    
   
class ProductUpdate(View):

    def get(self,request,product_id):

        product = Product.objects.get(pk=product_id)
        form = ProductForm(instance=product)

        return render(request = request,template_name = 'product_update.html',context = {'product':product,'form':form})
    
    def post(self,request,product_id):

        product = Product.objects.get(pk=product_id)
        form = ProductForm(request.POST,instance=product)

        if form.is_valid():
            product = form.save()
        
        return render(request = request,template_name = 'product_update.html',context = {'product':product,'form':form})


class ProductDelete(View):

    def get(self,request,product_id=None):

        if product_id:
            product = Product.objects.get(pk=product_id)
        else:
            product = Product()

        form = ProductForm(instance=product)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'product_delete.html',context = {'product':product,'form':form})
    
    def post(self,request,product_id=None):

        product = Product.objects.get(pk=product_id)

        form = ProductForm(request.POST,instance=product)

        product.delete()

        return redirect(reverse("product_list"))
    
# Customer List
class CustomerListView(View):
    def get(self, request):
        customers = Customer.objects.all()
        return render(request, 'customer_list.html', {'customers': customers})

# Customer Add
class CustomerAdd(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'customer_add.html', {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        return render(request, 'customer_add.html', {'form': form})

# Customer Update
class CustomerUpdate(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = CustomerForm(instance=customer)
        return render(request, 'customer_update.html', {'form': form, 'customer': customer})

    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        return render(request, 'customer_update.html', {'form': form, 'customer': customer})

# Customer Delete
class CustomerDelete(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, 'customer_delete.html', {'customer': customer})

    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return redirect('customer_list')