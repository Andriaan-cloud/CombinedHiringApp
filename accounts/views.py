
from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def home(request):
    context = {}
    return render(request,'accounts/home.html', context)

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            print('Data Saved')
            return redirect('home')

    user_form = ProfileForm()
    return render(request, 'accounts/profile.html', {'form': user_form})