from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('profile', views.profile, name='profile'),
    path('products/', views.products_index, name='index'),
]