from django.urls import path
from .views import (
    ProductListView, 
    CustomerListView, CustomerAdd, CustomerUpdate, CustomerDelete, 
    ProductAdd, ProductDetails, ProductUpdate, ProductDelete
)

urlpatterns = [
    # Product-related paths
    path('shop/', ProductListView.as_view(), name="product_list"),
    path('product_add/', ProductAdd.as_view(), name="product_add"),
    path('product_details/<int:product_id>/', ProductDetails.as_view(), name='product_details'),
    path('product_update/<int:product_id>/', ProductUpdate.as_view(), name='product_update'),
    path('product_delete/<int:product_id>/', ProductDelete.as_view(), name='product_delete'),
    
    # Customer-related paths
    path('customers/', CustomerListView.as_view(), name="customer_list"),
    path('customers/add/', CustomerAdd.as_view(), name='customer_add'),
    path('customers/update/<int:pk>/', CustomerUpdate.as_view(), name='customer_update'),
    path('customers/delete/<int:pk>/', CustomerDelete.as_view(), name='customer_delete'),
]
