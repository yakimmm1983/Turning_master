from django.db import models
import datetime
class regUser(models.Model):
    id = models.AutoField(primary_key=True )
    nickname = models.CharField(max_length=20, blank=True,null=False,unique=True)
    birthday = models.DateField(blank=True,null=False)
    password = models.CharField(max_length=10,blank=False,null=False)

class textPage(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(null=True,blank=True)
    img = models.CharField(max_length=256,null=True,blank=True)


