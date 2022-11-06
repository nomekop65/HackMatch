from django.db import models
from django.http import Http404
from HackMatch.models import profile, framework, language, stack
from django.shortcuts import render,redirect
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from forms import CustomUserCreationForm
from django.forms.models import model_to_dict

def getUserById(profile_id):
    return profile.objects.get(profile_id=id)

def getFrameworkById(framework_id):
    return framework.objects.get(framework_id=id)

def getLanguageById(profile_id):
    return language.objects.get(profile_id=id)

def getStackById(profile_id):
    return stack.objects.get(profile_id=id)

def getAllUsers():
    return profile.objects.all()

def getAllFrameworks():
    return framework.objects.all()

def getAllLanguages():
    return language.objects.all()

def loginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'templates/index.html')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Username/Password invalid')
            return render(request, 'templates/login.html')
    else:
        return render(request, 'templates/login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return render(request, 'movies/index.html')

def registerUser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful!")
            return render(request, 'templates/index.html')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'templates/register.html', context)
