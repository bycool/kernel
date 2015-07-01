from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


# Create your models here.

class UserFile(models.Model):
	Uername = models.CharField(max_length=30)
	filename = models.CharField(max_length=50)
	filepname = models.CharField(max_length=255)


