from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Gear(models.Model):
    CATEGORY = (
        ('Peripherals', 'Peripherals'),
        ('Hardware', 'Hardware'),
        ('Software', 'Software'),
        ('Miscellaneous', 'Miscellaneous')
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.CharField(max_length=10, null=True)
    profile_pic = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name

class Comment(models.Model):
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    gear = models.ForeignKey(Gear, null=True, on_delete=models.SET_NULL)
    comment = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.comment

    
