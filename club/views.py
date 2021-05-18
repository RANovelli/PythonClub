from django.shortcuts import get_object_or_404, render
from .models import Resource, Meeting, MeetingMinutes, Event

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def getResources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})

def getMeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list': meeting_list})

def meetingDetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetail.html', {'meeting': meeting})    
