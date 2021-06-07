from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.getResources, name='resources'),
    path('meetings/', views.getMeetings, name='meetings'),
    path('meetingDetail/<int:id>', views.meetingDetail, name='detail'),
    path('newresource/', views.newResource, name='newresource'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
