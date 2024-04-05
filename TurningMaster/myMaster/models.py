from django.db import models

class regUser(models.Model):
    id = models.AutoField(primary_key=True )
    nickname = models.CharField(max_length=20, blank=False,null=False)
    birthday = models.DateField()
    password = models.CharField(max_length=10,blank=False,null=False)

class textPage(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    img = models.CharField()

class enterUser(models.Model):               #этот класс нужен или нет?
    id = models.AutoField(primary_key=True)
    enter = models.OneToOneField(regUser)

