from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TextField(null=True, blank=True)
    meetinglocation=models.TextField(null=True, blank=True)
    meetingagenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingtitle

        class Meta:
            db_table='meeting'

class MeetingMinutes(models.Model):
    minutes=models.CharField(max_length=255)
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)

    def __str__(self):
        return self.minutes

        class Meta:
            db_table='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.TextField(null=True, blank=True)
    resourceurl=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resourcename

        class Meta:
            db_table='resource'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    location=models.TextField(null=True, blank=True)
    date=models.DateField()
    time=models.TextField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle

        class Meta:
            db_table='event'            



