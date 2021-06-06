from django.shortcuts import render, redirect
from .models import Profile
from .forms import CustomUserCreationForm
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.user.is_superuser:
        messages.error(request, 'You are already signed up and logged in!!')
        return redirect('all_customers')

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'there was a problem with your signup data, please try again')
    return render(request, 'registration/signup.html', {'signupform':form})
