from django.urls import path
from .views import ProductListView, CustomerList,ProductAdd
from . import views

urlpatterns = [
    path('shop/', ProductListView.as_view(), name="product_list"),
    path('customer/',CustomerList.as_view(), name="customer_list"),
    path('product_add/', views.ProductAdd.as_view(), name = "product_add"),
    path('product_details/<int:product_id>/', views.ProductDetails.as_view(), name='product_details'),
    path('product_update/<int:product_id>/', views.ProductUpdate.as_view(), name='product_update'),
    path('product_delete/<int:product_id>/', views.ProductDelete.as_view(), name='product_delete'),
]