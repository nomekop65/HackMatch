from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('events', views.events, name='events'),
    path('findTeam', views.findTeam, name='findTeam'),
    path('submitRequirement', views.submitRequirement, name='submitRequirement'),
    path('processApiToken', views.processApiToken, name='processApiToken')
]