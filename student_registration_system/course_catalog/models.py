from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # Add if needed
    credits = models.IntegerField()
    department = models.CharField(max_length=100, blank=True, null=True)  # Add if needed

    def __str__(self):
        return self.title