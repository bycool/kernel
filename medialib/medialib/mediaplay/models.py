from django.db import models

# Create your models here.

class userinfo(models.Model):
	userid = models.AutoField(primary_key=True)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=128)
	email = models.EmailField()

class mediafile(models.Model):
	fileid = models.AutoField(primary_key=True)
	filename = models.CharField(max_length=30)
	filesize = models.IntegerField()
	filetype = models.CharField(max_length=20)

class storagestate(models.Model):
	stateid = models.AutoField(primary_key=True)
	state_uid = models.IntegerField()
	state_fid = models.IntegerField()
	file_url = models.CharField(max_length=256)
	file_date_joined = models.DateField()
	examine = models.IntegerField()
	
	


