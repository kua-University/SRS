"""
URL configuration for student_registration_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from academic_progress import academic_views 
from course_catalog import course_views  # Rename the import
from user_management import user_views  # Rename the import
from registration import register_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('registrations/', include('registration.urls')),
    path('courses/', include('course_catalog.urls')),
    path('academic_progress/', include('academic_progress.urls')),
    path('users/', include('user_management.urls')),
]