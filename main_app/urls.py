from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.splash, name='splash'),

    path('profile/', views.profile, name='profile'),

    path('reviews/', views.reviews_index, name='index'),

    path('reviews/<int:review_id>', views.review_detail, name='detail'),

    path('reviews/user/', views.person, name='person'),

    path('create_comment/', views.createComment, name='create_comment'),

    path('accounts/register/', views.register, name='register'),
]