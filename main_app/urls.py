from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.splash, name='splash'),

    path('profile/', views.profile, name='profile'),

    path('reviews/', views.reviews_index, name='index'),

    path('reviews/<int:review_id>/', views.review_detail, name='detail'),

    path('user/', views.person, name='person'),

    path('create_comment/<int:review_id>/', views.create_comment, name='create_comment'),

    path('create_comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),

    path('create_comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

    path('accounts/register/', views.register, name='register'),
]