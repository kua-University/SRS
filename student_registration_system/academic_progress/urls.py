from django.urls import path
from .academic_views import enrollment_list, enrollment_create, enrollment_edit

urlpatterns = [
    path('', enrollment_list, name='enrollment_list'),
    path('add/', enrollment_create, name='enrollment_create'),
    path('edit/<int:pk>/', enrollment_edit, name='enrollment_edit'),
]