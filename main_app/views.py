from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import *

# Define the home view
def splash(request):
    return render(request, 'splash.html')

def products_index(request):
    products = Gear.objects.all()
    return render(request, 'products/index.html', {'products': products})

def profile(request):
    return render(request, 'profile.html')

def person(request):
    products = Gear.objects.all()
    comments = Comment.objects.all()
    context = {
        'products': products,
        'comments': comments,
    }
    return render(request, 'products/person.html', context)
