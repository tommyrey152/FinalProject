from django.urls import path, include
from . import views
from cart.views import OrderListView
from .views import (
    ProductListView, 
    CustomerListView, CustomerAdd, CustomerUpdate, CustomerDelete, 
    ProductAdd, ProductDetails, ProductUpdate, ProductDelete,
    LoginView, AdminHomeView, CustomerProductListView, SearchResultsView, MensProductsView, WomensProductsView,
    CustomerCreationForm,InventoryListView, InventoryListView,UpdateQuantityView, ProfileView, ProfileUpdateView, TrackOrderView, TrackOrderResultView, monthly_reports,
    CostReportList, CostReportCreate, CostReportUpdate, CostReportDelete, CostReportDetail, CostReportListView

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

    #MarketingCampaign-related paths
    path('marketingCampaign_list/', views.MarketingCampaignListView.as_view(), name="marketingCampaign_list"),
    path('marketingCampaign_add/', views.MarketingCampaignAdd.as_view(), name='marketingCampaign_add'),
    path('marketingCampaign_update/<int:pk>/', views.MarketingCampaignUpdate.as_view(), name='marketingCampaign_update'),
    path('marketingCampaign_delete/<int:pk>/', views.MarketingCampaignDelete.as_view(), name='marketingCampaign_delete'),
    path('marketingCampaign_details/<int:marketingCampaign_id>/', views.MarketingCampaignDetails.as_view(), name='marketingCampaign_details'),
    
    #Profile Paths
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('track_order/', TrackOrderView.as_view(), name='track_order'),
    path('track_order_result/', TrackOrderResultView.as_view(), name='track_order_result'),

    
    
    
    
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

    
    #inventory page
   path('inventory/', InventoryListView.as_view(), name='inventory_list'),
   path('product/<int:pk>/update_quantity/', UpdateQuantityView.as_view(), name='update_quantity'),
   
   #order list
   path('orders/', OrderListView.as_view(), name='orders_list'),
    
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('account_signup/', views.signup_view, name='account_signup'),

    path('reports/', monthly_reports, name='monthly_reports'),



    #cost Reports
    path('cost_reports/', CostReportList.as_view(), name='cost_report_list'),
    path('cost_reports/add/', CostReportCreate.as_view(), name='cost_report_add'),
    path('cost_reports/<int:pk>/', CostReportDetail.as_view(), name='cost_report_detail'),
    path('cost_reports/<int:pk>/update/', CostReportUpdate.as_view(), name='cost_report_update'),
    path('cost_reports/<int:pk>/delete/', CostReportDelete.as_view(), name='cost_report_delete'),
    path('cost_reports/', CostReportListView.as_view(), name='cost_report_list'),
]

# Add the following line at the end of your urlpatterns
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
