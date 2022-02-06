from django.db import models
from datetime import datetime

class Meals(models.Model):
    title = models.CharField(max_length=255)
    ingridients = models.TextField()
    image = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title

class Reserve(models.Model):
    ReserveID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    input_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.ReserveID)+' '+str(self.name)

class Users(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.IntegerField()

    def __str__(self):
        return str(self.id)+' '+str(self.username)

class Users(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.IntegerField()

    def __str__(self):
        return str(self.id)+' '+str(self.username)

class InterfaceControl(models.Model):
    ID = models.AutoField(primary_key=True, db_index=True)
    PARENTID = models.IntegerField(db_index=True)
    MAPPING = models.CharField(max_length=30, db_index=True)
    SORT = models.IntegerField(null=True, blank=True)
    FIELD_NAME = models.CharField(max_length=50, null=True, blank=True)
    TEXT = models.CharField(max_length=150, null=True, blank=True)
    FOR_WHOM = models.BooleanField(default=0)   # user or admin

    def __str__(self):
        return str(self.FIELD_NAME)+' '+str(self.TEXT)