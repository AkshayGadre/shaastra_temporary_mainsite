from django import forms
from django.db import models
from events.models import *
from users.models import *
from mainsite_2014.settings import DATABASES
erp_db = DATABASES.keys()[1]
from time import gmtime,strftime

#Also set is_active to True each time created
class TeamEvent(models.Model):
    team_id     = models.CharField(default='0',null=True,max_length = 50)
    team_name   = models.CharField(max_length = 30,blank = True,null=True)
    users       = models.ManyToManyField(User, blank = True, null = True)
    is_active   = models.BooleanField(default = False)
    #permissions = models.ManyToManyField(Permission, blank = True, null = True)
    event_id       = models.IntegerField(default=-1)#This will store id of participant event
    def size(self):
        return len(self.users.all())
        
    def save(self, *args, **kwargs):
        #Here, for event title, TODO:shorthand version of the name needed, for now truncated
        if self.event_id!=-1 and self.is_active == True:
            try:
               event=ParticipantEvent.objects.using(erp_db).get(id=self.event_id)
               self.team_id = 'TEAM#'+ str(event.title[:5])+'#'+str(self.pk)
            except:
                self.team_id = 'TEAM#'+ '#'+str(self.pk)
        super(TeamEvent, self).save(*args, **kwargs)
    def get_event(self):
        try:
            event =  ParticipantEvent.objects.using(erp_db).get(id = self.event_id)    
            return event
        except:
            return None
    def clean(self):
        super(TeamEvent,self).clean()
        try:
            if self.users.count() > ParticipantEvent.objects.using(erp_db).get(id=self.event_id).team_size_max:
                self.is_active = False
            if len(self.users.all())!=len(set(self.users.all())):
                # duplicate users
                self.is_active = False
        except:
            pass
    def __unicode__(self):
        try:
            event=ParticipantEvent.objects.using(erp_db).get(id=self.event_id)
            return "team id:%s - event:%s" % (self.team_id,event.title)
        except:
            return "team id:%s" % self.team_id

#Updates for each user:: The user will get this on login:: He has to approve

UPDATE_CHOICES = (
    ('Team Add', 'Team Add'),
    ('Deadline for Registration', 'Deadline for Registration'),
    )
    
class Update(models.Model):
    tag     = models.CharField(max_length = 20)
    content = models.CharField(max_length = 40)
    user    = models.ForeignKey(User, related_name = 'userupdates')
    #link    = models.?? on click user goes to where the update relates to
    
class TDP(models.Model):
    file_tdp         = models.FileField(max_length = 100,upload_to = 'tdpsubmissions')
    teamevent   = models.ForeignKey(TeamEvent,null = True,blank = True)
    
    def save(self):
        time =  strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()).replace(" ",'_')
        self.file_tdp.upload_to = 'tdpsubmissions/%s/%s_%s'%(self.teamevent.get_event().title,self.teamevent.team_id,time)
        super(TDP,self).save()
    def get_event(self):
        if event_id==-1:
            return None
        event = ParticipantEvent.objects.using(erp_db).get(id = teamevent.event_id)
        return event
        
def get_tdp_event(event = None):
    if event is None:
        return None
    if not isinstance(event,ParticipantEvent):
        return None
    tdplist=[]
    for tdp in TDP.objects.all():
        if tdp.get_event() == event:
            tdplist.append((tdp,tdp.teamevent.team_id))
    if len(tdplist) == 0:
        return None
    return tdplist
    

class TDPFileForm(forms.ModelForm):
    class Meta:
        model = TDP
        fields = ['file_tdp',]
