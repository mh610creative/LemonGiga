from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Define the home view
def splash(request):
    reviews = Gear.objects.order_by('date_created')
    return render(request, 'splash.html', {'reviews': reviews})

@login_required
def reviews_index(request):
    reviews = Gear.objects.order_by('date_created')
    return render(request, 'reviews/index.html', {'reviews': reviews})

@login_required
def review_detail(request, slug):
    review = Gear.objects.get(slug=slug)
    person = Person.objects.all()
    return render(request, 'reviews/detail.html', {'review': review, 'person': person})

@login_required
def profile(request):
    person = request.user.person
    form = PersonForm(instance=person)
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES,instance=person)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'profile.html', context)

@login_required
def person(request, slug):
    reviews = Gear.objects.all()
    person = Person.objects.get(slug=slug)
    comments = person.comment_set.all()
    context = {
        'reviews': reviews,
        'comments': comments,
        'person': person,
    }
    return render(request, 'reviews/person.html', context)

@login_required
def create_comment(request, review_id):
    review = Gear.objects.get(id=review_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.person = request.user.person
            comment.gear = review
            comment.save()
            return redirect('detail', slug=review.slug)
        else:
            print(form.errors)
    context = {
        'review': review,
        'form': form,
        'button': 'Create'
    }
    return render(request, 'forms/comment_form.html', context)

@login_required
def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('detail', slug=comment.gear.slug)
        else:
            print(form.errors)
    context = {
        'review': comment.gear,
        'form': form,
        'button': 'Edit'
    }
    return render(request, 'forms/comment_form.html', context)

def register(request):
    error_message = ''
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            new_person = Person(user=user, name=user.username, email=user.email, date_created=user.date_joined)
            new_person.save()
            login(request, user)
            return redirect('redirect')
        else:
            error_message = 'Invalid sign up - try again'
    form = CreateUserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/register.html', context)

@login_required
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('detail', slug=comment.gear.slug)
    context = {'comment': comment}
    return render(request,'forms/delete.html', context)

@login_required
def login_redirectview(request):
    return redirect('person', slug=request.user.person.slug)







