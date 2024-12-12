from django.shortcuts import render, redirect, get_object_or_404
from user_management.models import Student
from course_catalog.models import Course
from .models import Enrollment
from .forms import EnrollmentForm  # Make sure you have this form defined
from .models import Student  # Ensure this is correct

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment_list.html', {'enrollments': enrollments})

def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollment_form.html', {'form': form})

def enrollment_edit(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, 'enrollment_form.html', {'form': form})