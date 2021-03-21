from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from .models import *

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email']

class LoginForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

class PersonForm(ModelForm):
    
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ['user']
        
