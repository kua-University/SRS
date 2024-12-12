from django.db import models
from django.conf import settings  # For using User model
from course_catalog.models import Course

class Registration(models.Model):
    student = models.ForeignKey('user_management.Student', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} registered for {self.course}"