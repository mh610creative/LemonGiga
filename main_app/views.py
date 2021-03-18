from django.shortcuts import render

from django.http import HttpResponse

# Define the home view
def splash(request):
    return render(request, 'products/dashboard.html')

def products_index(request):
    return render(request, 'products/index.html')

def profile(request):
    return render(request, 'profile.html')
