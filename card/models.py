from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    ctype = models.CharField(max_length=20)
    bname = models.CharField(max_length=20)
    bqoute = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    ofPhone = models.CharField(max_length=50)
    to = models.CharField(max_length=50, null=True)
    detail = models.CharField(max_length=200, null=True)
    timeMeeting = models.DateTimeField(null=True)
    timeCreated = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.bname+" "+self.name+" "+self.to





