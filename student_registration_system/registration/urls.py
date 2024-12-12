from django.urls import path
from .register_views import registration_list, registration_create, registration_edit

urlpatterns = [
    path('', registration_list, name='registration_list'),
    path('add/', registration_create, name='registration_create'),
    path('edit/<int:pk>/', registration_edit, name='registration_edit'),
]