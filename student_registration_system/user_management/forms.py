from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile  # Ensure this line is correct

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['bio']  # Add any additional fields here