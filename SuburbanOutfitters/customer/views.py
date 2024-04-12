from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, Customer, Category, ProductSize
from .forms import ProductForm, CustomerForm, LoginForm
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.forms import inlineformset_factory


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_form'] = CustomerForm()
        return context

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            if user.is_superuser:  
                return redirect('admin_home')
            else:
                return redirect('home')
        else:
            messages.error(self.request, 'Invalid username or password.')
            return self.render_to_response(self.get_context_data(form=form))


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
            # Redirect to the product list page
            return redirect('product_list')
        # If the form isn't valid, render the page again with form errors
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
    
    
ProductSizeFormset = inlineformset_factory(Product, ProductSize, fields=('size', 'quantity',))

def product_add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            formset = ProductSizeFormset(request.POST, instance=product)
            if formset.is_valid():
                formset.save()
                # Redirect to product list or product detail
                return redirect('product_list')
    else:
        form = ProductForm()
        formset = ProductSizeFormset()
    
    return render(request, 'product_add.html', {'form': form, 'formset': formset})
    
    
    
    
    
    
    
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
