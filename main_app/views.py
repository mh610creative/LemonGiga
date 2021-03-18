from django.shortcuts import render

from django.http import HttpResponse
from .models import *

# Define the home view
def splash(request):
    return render(request, 'products/dashboard.html')

def products_index(request):
    products = Gear.objects.all()
    return render(request, 'products/index.html', {'products': products})

def profile(request):
    return render(request, 'profile.html')
