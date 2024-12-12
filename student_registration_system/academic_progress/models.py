from django.db import models
from user_management.models import Student
from django.utils import timezone  # Import timezone

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    enrollment_date = models.DateField(default=timezone.now)  # Set default to current date

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course}"