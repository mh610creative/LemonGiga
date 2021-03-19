from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['person', 'gear','comment']

