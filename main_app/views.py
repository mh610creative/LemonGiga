from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import login
from .models import *
from .forms import *

# Define the home view
def splash(request):
    return render(request, 'splash.html')

def reviews_index(request):
    reviews = Gear.objects.all()
    return render(request, 'reviews/index.html', {'reviews': reviews})

def review_detail(request, review_id):
    review = Gear.objects.get(id=review_id)
    return render(request, 'reviews/detail.html', {'review': review })

def profile(request):
    return render(request, 'profile.html')

def person(request):
    reviews = Gear.objects.all()
    comments = Comment.objects.all()
    context = {
        'reviews': reviews,
        'comments': comments,
    }
    
    return render(request, 'reviews/person.html', context)

def createComment(request):
    reviews = Gear.objects.all()
    comments = Comment.objects.all()
    form = CommentForm()
    context = {
        'reviews': reviews,
        'comments': comments,
        'form': form
    }
    return render(request, 'forms/comment_form.html', context)

def register(request):
    error_message = ''
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request)
            return redirect('person')
        else:
            error_message = 'Invalid sign up - try again'
    form = CreateUserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/register.html', context)

def login(request):
    error_message = ''
    if request.method == 'GET':
        form = LoginForm(request.GET)
        if form.is_valid():
            login(request)
            return redirect('person')
        else:
            error_message = 'Invalid sign up - try again'
    form = LoginForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/login.html', context)




        





