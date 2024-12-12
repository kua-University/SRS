# academic_progress/forms.py
from django import forms
from .models import Enrollment

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'enrollment_date']  # Update these fields to match your model