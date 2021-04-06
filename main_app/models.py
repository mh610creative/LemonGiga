from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            slug = slugify(self.name)
            self.slug = slug[:50]
        return super().save(*args, **kwargs)

class Gear(models.Model):
    CATEGORY = (
        ('Peripherals', 'Peripherals'),
        ('Hardware', 'Hardware'),
        ('Software', 'Software'),
        ('Miscellaneous', 'Miscellaneous')
    )
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.CharField(max_length=10, null=True)
    pack_shot = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            slug = slugify(self.name)
            self.slug = slug[:50]
        return super().save(*args, **kwargs)

class Comment(models.Model):
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    gear = models.ForeignKey(Gear, null=True, on_delete=models.SET_NULL)
    comment = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.comment

    
