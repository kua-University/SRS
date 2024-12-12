# user_management/models.py
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Use string reference
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Use string reference
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username