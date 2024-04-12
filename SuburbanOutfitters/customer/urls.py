from django.urls import path, include
from . import views
from .views import (
    ProductListView, 
    CustomerListView, CustomerAdd, CustomerUpdate, CustomerDelete, 
    ProductAdd, ProductDetails, ProductUpdate, ProductDelete,
    LoginView, AdminHomeView
)

urlpatterns = [
    # Product-related paths
    path('products/', ProductListView.as_view(), name="product_list"),
    path('prodcuts/add/', ProductAdd.as_view(), name="product_add"),
    path('prodcuts/details/<int:product_id>/', ProductDetails.as_view(), name='product_details'),
    path('prodcuts/update/<int:product_id>/', ProductUpdate.as_view(), name='product_update'),
    path('prodcuts/delete/<int:product_id>/', ProductDelete.as_view(), name='product_delete'),
    
    # Customer-related paths
    path('customers/', CustomerListView.as_view(), name="customer_list"),
    path('customers/add/', CustomerAdd.as_view(), name='customer_add'),
    path('customers/update/<int:pk>/', CustomerUpdate.as_view(), name='customer_update'),
    path('customers/delete/<int:pk>/', CustomerDelete.as_view(), name='customer_delete'),


    #admin-related Paths
    path('admin_home/', views.AdminHomeView.as_view(), name='admin_home'),

    #login path
    path('login/', views.LoginView.as_view(), name='login'),

    
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('account_signup/', views.signup_view, name='account_signup'),
    
  
]
