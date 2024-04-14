from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, Customer, Category, MarketingCampaign,Sale,Cost
from .forms import (
    ProductForm, CustomerForm, LoginForm, CustomerCreationForm, MarketingCampaignForm, ProfileUpdateForm
)
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
from django import forms
from django.http import JsonResponse
from django.views import View
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import Profile
from django.utils import timezone
from django.db.models import Sum
from datetime import datetime
from datetime import timedelta
from cart.models import Order
from django.http import JsonResponse
from django.core.exceptions import ValidationError

class InventoryListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'inventory_list.html'
    queryset = Product.objects.all().order_by('productName')
    

class UpdateQuantityView(View):
    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        new_quantity = request.POST.get('quantity')
        product = Product.objects.get(pk=product_id)
        product.quantity = new_quantity
        product.save()
        return JsonResponse({'status': 'success', 'new_quantity': new_quantity})
    

class InventoryListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'inventory_list.html'
    queryset = Product.objects.all().order_by('productName')

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
            return redirect('login')
            #return redirect('login')


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
    

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile
    


class MarketingCampaignListView(View):
    def get(self, request):
        marketingCampaigns = MarketingCampaign.objects.all()
        return render(request, 'marketingCampaign_list.html', {'marketingCampaigns': marketingCampaigns})

# Marketing Add
class MarketingCampaignAdd(View):
    def get(self, request):
        form = MarketingCampaignForm()
        return render(request, 'marketingCampaign_add.html', {'form': form})

    def post(self, request):
        form = MarketingCampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marketingCampaign_list')
        return render(request, 'MarketingCampaign_add.html', {'form': form})

# Marketing Update
class MarketingCampaignUpdate(View):
    def get(self, request, pk):
        marketingCampaign = get_object_or_404(MarketingCampaign, pk=pk)
        form = MarketingCampaignForm(instance=marketingCampaign)
        return render(request, 'marketingCampaign_update.html', {'form': form, 'marketingCampaign': marketingCampaign})

    def post(self, request, pk):
        marketingCampaign = get_object_or_404(MarketingCampaign, pk=pk)
        form = MarketingCampaignForm(request.POST, instance=marketingCampaign)
        if form.is_valid():
            form.save()
            return redirect('marketingCampaign_list')
        return render(request, 'marketingCampaign_update.html', {'form': form, 'marketingCampaign': marketingCampaign})

# Marketing Delete
class MarketingCampaignDelete(View):
    def get(self, request, pk):
        marketingCampaign = get_object_or_404(MarketingCampaign, pk=pk)
        return render(request, 'marketingCampaign_delete.html', {'marketingCampaign': marketingCampaign})

    def post(self, request, pk):
        marketingCampaign = get_object_or_404(MarketingCampaign, pk=pk)
        marketingCampaign.delete()
        return redirect('marketingCampaign_list')
    
# Marketing Details
class MarketingCampaignDetails(View):
    def get(self,request,marketingCampaign_id=None):
        if marketingCampaign_id:
            marketingCampaign = MarketingCampaign.objects.get(pk=marketingCampaign_id)
        else:
            marketingCampaign = MarketingCampaign()
        form = MarketingCampaignForm(instance=marketingCampaign)
        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'marketingCampaign_details.html',context = {'marketingCampaign':marketingCampaign,'form':form})
    
    def post(self,request,marketingCampaign_id=None):
        return redirect(reverse("marketingCampaign_list"))

#monthly reporting
def monthly_reports(request):
    # Get current month and year
    now = datetime.now()
    current_month = now.month
    current_year = now.year

    # Calculate gross sales for the current month
    gross_sales = Sale.objects.filter(date__month=current_month, date__year=current_year).aggregate(Sum('amount'))['amount__sum'] or 0

    # Calculate total costs for the current month
    total_costs = Cost.objects.filter(date__month=current_month, date__year=current_year).aggregate(Sum('amount'))['amount__sum'] or 0

    # Calculate net profit for the current month
    net_profit = gross_sales - total_costs

    context = {
        'gross_sales': gross_sales,
        'total_costs': total_costs,
        'net_profit': net_profit,
    }
    return render(request, 'reports.html', context)


class ProfileUpdateView(View):
    def get(self, request):
        profile = request.user.profile
        form = ProfileUpdateForm(instance=profile)
        return render(request, 'profile_update.html', {'form': form})

    def post(self, request):
        profile = request.user.profile
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'profile_update.html', {'form': form})
    

class TrackOrderView(View):
    def get(self, request):
        return render(request, 'track_order_result.html')

    def post(self, request):
        order_id = request.POST.get('order_id')
        try:
            order = Order.objects.get(id=order_id)
            days_since_order = (timezone.now() - order.date_ordered).days

            if days_since_order <= 5:
                status = 'PENDING'
            elif 5 < days_since_order <= 10:
                status = 'SHIPPED'
            else:
                status = 'DELIVERED'

            context = {
                'status': status
            }
        except Order.DoesNotExist:
            context = {
                'status': 'ORDER NOT FOUND'
            }

        return render(request, 'track_order_result.html', context=context)