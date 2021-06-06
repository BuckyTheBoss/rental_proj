from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('customer/', views.CustomerListView.as_view(), name='all_customers'),
    path('customer/add', views.CustomerCreateView.as_view(), name='create_customer'),
    path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('vehicle/<int:pk>', views.VehicleDetailView.as_view(), name='vehicle_detail'),
    path('customer/update/<int:pk>', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('type/update/<int:pk>', views.VehicleTypeUpdateView.as_view(), name='type_update'),
    path('vehicle/add', views.create_vehicle, name='create_vehicle'),
    path('multivehicle/add', views.create_multi_vehicle, name='create_multi_vehicle'),
    path('rental/add', views.add_rentals, name='create_rentals'),
    path('rental/', views.RentalListView.as_view(), name='all_rentals'),
    path('type/', views.VehicleTypeListView.as_view(), name='all_types'),

]