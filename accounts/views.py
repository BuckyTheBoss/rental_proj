from django.shortcuts import render, redirect
from .models import Profile
from .forms import CustomUserCreationForm
# Create your views here.

def signup(request):
    if request.user.is_superuser:
        return redirect('all_customers')

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login')
    return render(request, 'registration/signup.html', {'form':form})
