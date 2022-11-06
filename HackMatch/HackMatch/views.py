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

def reverseInsort(list, vaule, key):
    begining=0
    end = len(list)

    while begining < end:
        middle = (begining+end)//2

        if key > len(list[middle][1]): 
          end = middle
        else: 
          begining = middle+1
    list.insert(begining, vaule)

def sortuserbyscore(eventmemberjson):

    #get user that need team and store in a list
    eventneedteamdict={i:eventmemberjson["users"][i] for i in eventmemberjson["users"] if eventmemberjson["users"][i]["searchingForMember"]==True}
    requirementSet=set(eventmemberjson["requirement"])
    userScoreList=[]
    for userid in eventneedteamdict:  
        requirementMeetList = list(requirementSet.intersection(set(eventneedteamdict[userid]["skills"])))
        print(userid)
        print(requirementMeetList)
        reverseInsort(userScoreList,(userid,requirementMeetList,eventneedteamdict[userid]["username"]), len(requirementMeetList)) #save user id and score as a tuple and sort greatest to lowest

    return userScoreList

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

def populaterequirement(request):
    if request.method== "POST":
        skilllist=request.POST['skills']
        skilllist=[i.lower() for i in skilllist]
        eventmemberjson={"users":{},"requirement":skilllist}
        usersqueryset= getAllUsers.filter()
        usersqueryset=usersqueryset.objects.values('id','stacks','languages','framework','proficiencyLevel','searchingForMembers','username')
        usersdict={i['id']:{"skills":[i['stacks']+i['languages']+i['framework']+['proficiencyLevel']],"searchingForMember":i['searchingForMember'],"username":i['username']} for i in usersqueryset}
        eventmemberjson["users"]=usersdict
        eventmemberjson["users"]={}
        return sortuserbyscore(eventmemberjson)

def processapitoken(request,token):
    if request.method == "POST":
        
        mlhrequest=requests.get(f"https://my.mlh.io/api/v3/user.json?access_token={token}")
        if mlhrequest['data']['id'] == 354004:
            return render(request, 'templates/index.html')
def index(request):
    return render(request, 'index.html')