from django.shortcuts import render, redirect
from django.views import generic
from .models import Customer
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


class CustomerListView(generic.ListView):
    queryset = Customer.objects.all().order_by('first_name', 'last_name')
    context_object_name = 'helloworld'

class CustomerCreateView(generic.CreateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('all_customers')


class CustomerDetailView(generic.DetailView):
    model = Customer
    # template_name = 'mycustomer.html'

class CustomerUpdateView(generic.UpdateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('all_customers')


def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'registration/signup.html', {'form':form})
