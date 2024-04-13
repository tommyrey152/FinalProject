from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('detail/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/complete/', views.checkout_complete, name='checkout_complete'),
]
