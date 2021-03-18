from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

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

    
