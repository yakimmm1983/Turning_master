from django.db import models

class regUser(models.Model):
    id = models.AutoField(primary_key=True )
    nickname = models.CharField(max_length=20, blank=False,null=False)
    birthday = models.DateField(null=True,blank=True)
    password = models.CharField(max_length=10,blank=False,null=False)

class textPage(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(null=True,blank=True)
    img = models.CharField(max_length=256,null=True,blank=True)


