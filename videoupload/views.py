from django.shortcuts import render
from .models import videoupload

# Create your views here.
def index(request):
    videoupload= Video.objects.all()
    return render(request, 'index.html',{"videoupload":videoupload})

