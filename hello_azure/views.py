from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import webbrowser

def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')


def events(request):
    return render(request, 'hello_azure/events.html')

def findTeam(request):
    return render(request, 'hello_azure/findTeam.html')

def processApiToken(request):
    link=request.POST['loginin']
    print(link)
    webbrowser.open(link)
    return render(request, 'hello_azure/index.html')


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

@csrf_exempt
def submitRequirement(request):
    if request.method== "POST":
        skillList=request.POST.getlist('skills[]')
        skillList=[i.lower() for i in skillList]
        eventmemberjson={
        0:{"skills":["frontend","java","skilled"],"searchingForMember":True,"username":"John Smith"},
        15:{"skills":["frontend","backend","python","java","beginner"],"searchingForMember":False,"username":"Jame Smith"},
        1:{"skills":["frontend","python","java","django","skilled"],"searchingForMember":True,"username":"Jane Smith"},
        34:{"skills":["frontend","backend","python","java","django","skilled"],"searchingForMember":True,"username":"Bob Bill"},
        45:{"skills":["frontend","backend","python","java","django","beginner"],"searchingForMember":False,"username":"Bill Jone"},
        73:{"skills":["backend","python","java","beginner"],"searchingForMember":True,"username":"Richard"},
        19:{"skills":["frontend","java","django","beginner"],"searchingForMember":False,"username":"Zach"},
        20:{"skills":["frontend","java","skilled"],"searchingForMember":True,"username":"Hannah"},
        35:{"skills":["frontend","backend","python","java","beginner"],"searchingForMember":False,"username":"Ian"},
        41:{"skills":["backend","python","java","skilled"],"searchingForMember":True,"username":"John"},
        54:{"skills":["frontend","backend","python","java","django","skilled"],"searchingForMember":True,"username":"Juan"},
        65:{"skills":["frontend","backend","python","django","beginner"],"searchingForMember":True,"username":"Mary"},
        93:{"skills":["backend","python","java","beginner"],"searchingForMember":True,"username":"Aaron"},
        29:{"skills":["frontend","django","skilled"],"searchingForMember":True,"username":"Eric"}
        }
        #get user that need team and store in a list
        eventneedteamdict={i:eventmemberjson[i] for i in eventmemberjson if eventmemberjson[i]["searchingForMember"]==True}
        requirementSet=set(skillList)
        userScoreList=[]
        for userid in eventneedteamdict:  
            requirementMeetList = list(requirementSet.intersection(set(eventneedteamdict[userid]["skills"])))
            requirementMeetList=[i.capitalize() for i in requirementMeetList]
            reverseInsort(userScoreList,[userid,requirementMeetList,[eventneedteamdict[userid]["username"]]], len(requirementMeetList)) #save user id and score as a tuple and sort greatest to lowest
        
        stringnumber=["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
        context={stringnumber[i]:userScoreList[i][2]+userScoreList[i][1] for i in range(0,len(userScoreList))}
        
        print(context)
        return render(request,'hello_azure/matching.html',context)


@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name }
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')