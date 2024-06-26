from django.urls import path
from . import views
from . views import OrderDetailsView, OrderListView

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('detail/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/complete/', views.checkout_complete, name='checkout_complete'),
    path('<int:cart_item_id>/edit/', views.cart_edit, name='cart_edit'), 
    
    
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', OrderDetailsView.as_view(), name='order_details'),

]

