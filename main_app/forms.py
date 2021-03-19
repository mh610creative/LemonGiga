from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from .models import *

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['person', 'gear','comment']

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']
