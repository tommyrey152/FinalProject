from django.urls import path, include
from . import views
from .views import (
    ProductListView, 
    CustomerListView, CustomerAdd, CustomerUpdate, CustomerDelete, 
    ProductAdd, ProductDetails, ProductUpdate, ProductDelete,
    LoginView
)

urlpatterns = [
    # Product-related paths
    path('shop/', ProductListView.as_view(), name="product_list"),
    path('shop/add/', ProductAdd.as_view(), name="product_add"),
    path('shop/details/<int:product_id>/', ProductDetails.as_view(), name='product_details'),
    path('shop/update/<int:product_id>/', ProductUpdate.as_view(), name='product_update'),
    path('shop/delete/<int:product_id>/', ProductDelete.as_view(), name='product_delete'),
    
    # Customer-related paths
    path('customers/', CustomerListView.as_view(), name="customer_list"),
    path('customers/add/', CustomerAdd.as_view(), name='customer_add'),
    path('customers/update/<int:pk>/', CustomerUpdate.as_view(), name='customer_update'),
    path('customers/delete/<int:pk>/', CustomerDelete.as_view(), name='customer_delete'),
    
    path('men/', views.mens_products, name='mens_products'),
    path('women/', views.womens_products, name='womens_products'),
    path('products/', views.all_products, name='all_products'),
    
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('account_signup/', views.signup_view, name='account_signup'),
    
  
]
