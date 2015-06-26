from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


# Create your models here.

class NUblog(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateTimeField()

