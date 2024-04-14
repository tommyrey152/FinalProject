from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, Customer, Category
from .forms import (
    ProductForm, CustomerForm, LoginForm, CustomerCreationForm,
)
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django import forms
from django.http import JsonResponse
from django.views import View
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator




class InventoryListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'inventory_list.html'
    queryset = Product.objects.all().order_by('productName')
    
    
class UpdateQuantityView(View):
    def post(self, request, *args, **kwargs):
        try:
            product_id = kwargs.get('pk')
            new_quantity = request.POST.get('quantity')
            product = Product.objects.get(pk=product_id)
            product.quantity = new_quantity
            product.save()

            return JsonResponse({'new_quantity': new_quantity})
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class CustomerCreationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('username', 'password', 'firstName', 'lastName', 'address')

    def clean_password(self):
        return make_password(self.cleaned_data['password'])

class LoginForm(AuthenticationForm):
    pass

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            if user.is_superuser:
                return redirect('admin_home')
            else:
                return super().form_valid(form)
        else:
            messages.error(self.request, 'Invalid username or password.')
            return redect('login')



#Admin Views
class AdminHomeView(View):
    def get(self, request):
        return render(request, 'admin_home.html')

#productViews

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'product_list.html', context=context)


from django.shortcuts import redirect

class ProductAdd(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'product_add.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'product_add.html', {'form': form})


    

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

    def get(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        form = ProductForm(instance=product)
        return render(request, 'product_update.html', {'product': product, 'form': form})
    
    def post(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            # Redirect to the product list page
            return redirect('product_list')
        else:
            # If the form isn't valid, render the page again with form errors
            return render(request, 'product_update.html', {'product': product, 'form': form})



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
    
    
    


class ProductAdd(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'product_add.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'product_add.html', {'form': form})

    
    
    
    
    
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


class CustomerProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        print(products)  # Check if this query is returning products
        return render(request, 'customer_product_list.html', {'products': products})
    
    
    
class SearchResultsView(View):
    def get(self, request):
        query = request.GET.get('q', '')  # Retrieve the search query
        products = Product.objects.filter(
            productName__icontains=query
        ) | Product.objects.filter(
            description__icontains=query
        )
        return render(request, 'search_results.html', {'products': products})
    


class MensProductsView(ListView):
    model = Product
    template_name = 'mens_products.html'  # Updated to reference templates at the root
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(gender='M')

class WomensProductsView(ListView):
    model = Product
    template_name = 'womens_products.html'  # Updated to reference templates at the root
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(gender='W')