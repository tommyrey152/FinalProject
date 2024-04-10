from django.urls import path
from .views import ProductListView

urlpatterns = [
    path('shop/', ProductListView.as_view(), name="product_list"),
]