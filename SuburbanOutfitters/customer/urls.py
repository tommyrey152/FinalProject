from django.urls import path
from .views import ProductListView, CustomerList

urlpatterns = [
    path('shop/', ProductListView.as_view(), name="product_list"),
    path('customer/',CustomerList.as_view(), name="customer_list"),
]