from django.db import models
#from file_format import ContentTypeRestrictedFileField
from django.contrib.auth.models import User

class files_model(models.Model):
    title=models.CharField(max_length=100)
    attachment=models.FileField(upload_to='varun/')
    #user=models.OneToOneField(User)uncomment this after implementing login
