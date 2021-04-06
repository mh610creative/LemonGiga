from django.contrib import admin
from .models import Person, Gear, Comment


class GearAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

# Register your models here.
admin.site.register(Person)
admin.site.register(Gear, GearAdmin)
admin.site.register(Comment)
