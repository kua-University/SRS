from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm, StudentProfileForm
from .models import StudentProfile  # Ensure this import is here if needed

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = StudentProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')  # Redirect to a success page
    else:
        user_form = UserRegistrationForm()
        profile_form = StudentProfileForm()
    
    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

def profile_view(request):
    profile = StudentProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})