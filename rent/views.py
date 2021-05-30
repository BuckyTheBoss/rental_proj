from django.shortcuts import render
from django.views import generic
from .models import Customer
from django.urls import reverse_lazy
# Create your views here.


class CustomerListView(generic.ListView):
    queryset = Customer.objects.all().order_by('first_name', 'last_name')


class CustomerCreateView(generic.CreateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('all_customers')


class CustomerDetailView(generic.DetailView):
    model = Customer

class CustomerUpdateView(generic.UpdateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('all_customers')