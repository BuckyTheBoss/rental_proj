from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('customer/', views.CustomerListView.as_view(), name='all_customers'),
    path('customer/add', views.CustomerCreateView.as_view(), name='create_customer'),
    path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/update/<int:pk>', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('vehicle/add', views.create_vehicle, name='create_vehicle')
]