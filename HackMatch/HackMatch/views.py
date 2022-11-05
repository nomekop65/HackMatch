from django.db import models
from django.http import Http404
from connectivity.models import profile, framework, language, stack
from django.shortcuts import render,redirect
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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

# def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return render(request, 'movies/index.html')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Username/Password invalid')
            return render(request, 'members/login.html')
    else:
        return render(request, 'members/login.html')
