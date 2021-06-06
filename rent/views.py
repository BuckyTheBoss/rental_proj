from django.contrib import messages
from django.forms import formsets
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from .models import Customer, Rental, Vehicle, VehicleType
from .forms import VehicleForm, VehicleFormBasic, VehicleFormSet, RentalModelFormSet
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class CustomerListView(ListView):
    queryset = Customer.objects.all().order_by('first_name', 'last_name')
    context_object_name = 'helloworld'

class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = [
        'first_name', 
        'last_name',
        'email',
        'phone_number',
        'address',
        'city',
        'country',
        'pic'
        ]
    success_url = reverse_lazy('all_customers')

    def form_valid(self, form):
        customer = form.save(commit=False)
        customer.created_by = self.request.user.profile
        customer.save()
        return super().form_valid(form)


class CustomerDetailView(DetailView):
    model = Customer
    # template_name = 'rent/mycustomer.html'


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('all_customers')


@login_required
def create_vehicle(request):
    form = VehicleFormBasic()
    if request.method == 'POST':
        form = VehicleFormBasic(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            vehicle = Vehicle(**form.cleaned_data)
            vehicle.created_by = request.user.profile
            vehicle.save()
            redirect('all_customers')
    
    return render(request, 'rent/create_vehicle.html', {'form':form})



@login_required
def create_multi_vehicle(request):
    formset = VehicleFormSet()
    if request.method == 'POST':
        formset = VehicleFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data)
                vehicle = Vehicle(**form.cleaned_data)
                vehicle.created_by = request.user.profile
                vehicle.save()
            redirect('all_customers')
    
    return render(request, 'rent/multicreate_vehicle.html', {'formset':formset})


class VehicleDetailView(DetailView):
    model = Vehicle

class RentalListView(ListView):
    model = Rental

class VehicleTypeListView(ListView):
    model = VehicleType

class VehicleTypeUpdateView(UpdateView):
    model = VehicleType
    fields = '__all__'
    success_url = reverse_lazy('all_types')


def add_rentals(request):
    formset = RentalModelFormSet()
    if request.method == "POST":
        formset = RentalModelFormSet(request.POST)

        if formset.is_valid():
            formset.save()
            return redirect('all_rentals')
        else:
            messages.error(request, 'Bad form info was submitted, check specifics below')


    return render(request, 'rent/add_rental.html', {'formset':formset})
