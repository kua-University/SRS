from django.urls import path
from .course_views import course_list, course_create, course_edit

urlpatterns = [
    path('', course_list, name='course_list'),
    path('add/', course_create, name='course_create'),
    path('edit/<int:pk>/', course_edit, name='course_edit'),
]