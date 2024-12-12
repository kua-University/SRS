from django.urls import path
from .user_views import register, profile_view

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),
]