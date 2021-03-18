from django.contrib import admin
from .models import Person, Gear, Comment

# Register your models here.
admin.site.register(Person)
admin.site.register(Gear)
admin.site.register(Comment)
