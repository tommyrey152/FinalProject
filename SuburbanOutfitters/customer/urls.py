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
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_add/', views.ProductAdd.as_view(), name='product_add'),
    path('product_details/<int:product_id>/', views.ProductDetails.as_view(), name='product_details'),
    path('product_update/<int:product_id>/', views.ProductUpdate.as_view(), name='product_update'),
    path('product_delete/<int:product_id>/', views.ProductDelete.as_view(), name='product_delete'),


    
    # Customer-related paths
    path('customer_list/', views.CustomerListView.as_view(), name="customer_list"),
    path('customer_add/', views.CustomerAdd.as_view(), name='customer_add'),
    path('customer_update/<int:pk>/', views.CustomerUpdate.as_view(), name='customer_update'),
    path('customer_delete/<int:pk>/', views.CustomerDelete.as_view(), name='customer_delete'),

    # Product paths 


    #admin-related Paths
    path('admin_home/', views.AdminHomeView.as_view(), name='admin_home'),

    #login path
    path('login/', views.LoginView.as_view(), name='login'),

    
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('account_signup/', views.signup_view, name='account_signup'),
    
  
]
