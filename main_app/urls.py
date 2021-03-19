from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('profile/', views.profile, name='profile'),
    path('reviews/', views.products_index, name='index'),
    path('reviews/person/', views.person, name='person'),
    path('create_comment', views.createComment, name='create_comment'),

]