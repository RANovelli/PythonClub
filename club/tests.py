from club.forms import MeetingForm, ResourceForm
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Resource, Meeting
import datetime
from .forms import ResourceForm, MeetingForm

# Create your tests here.
class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resource(resourcename='Python Tutorial')
    
    def test_resourcestring(self):
        self.assertEqual(str(self.type), 'Python Tutorial')

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'club_resource')

class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='Python Intro')
        self.meeting=Meeting(meetingtitle='Intro', meetingdate=datetime.date(2021,5,24), meetingtime='5:00', meetinglocation='Vivace', meetingagenda='Python')
    
    def test_meetingstring(self):
        self.assertEqual(str(self.type), 'Python Intro')

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'club_meeting')

class NewResourceForm(TestCase):
    def test_resourceform(self):
        data={
            'resourcename':'Python Tutorial', 
            'resourcetype':'online class', 
            'resourceurl':'http://www.w3schools.com',
            'dateentered':'2021-6-01',
            'usedid':'Ryan',
            'description':'Python resource'
        }
        form=ResourceForm (data)
        self.assertTrue(form.is_valid)            