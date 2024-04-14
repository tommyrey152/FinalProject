from django.urls import path, include
from . import views
from .views import (
    ProductListView, 
    CustomerListView, CustomerAdd, CustomerUpdate, CustomerDelete, 
    ProductAdd, ProductDetails, ProductUpdate, ProductDelete,
    LoginView, AdminHomeView, CustomerProductListView, SearchResultsView, MensProductsView, WomensProductsView,
    CustomerCreationForm,
)

urlpatterns = [
    # Product-related paths
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_add/', views.ProductAdd.as_view(), name='product_add'),
    path('product_details/<int:product_id>/', views.ProductDetails.as_view(), name='product_details'),
    path('product_update/<int:product_id>/', views.ProductUpdate.as_view(), name='product_update'),
    path('product_delete/<int:product_id>/', views.ProductDelete.as_view(), name='product_delete'),
    
    path('customer_product_list/', CustomerProductListView.as_view(), name='customer_product_list'),


    
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
    path('create_account/', views.CustomerAdd.as_view(), name='create_account'),

    
    #search bar
    path('search/', SearchResultsView.as_view(), name='search_results'),
    
    path('mens/', MensProductsView.as_view(), name='mens_products'),
    path('womens/', WomensProductsView.as_view(), name='womens_products'),

    
    
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('account_signup/', views.signup_view, name='account_signup'),
    
  
]

# Add the following line at the end of your urlpatterns
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
