from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import *
from .forms import CommentForm

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


