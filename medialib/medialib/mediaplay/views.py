# Create your views here.

from django.template import loader, Context
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response

from medialib.mediaplay.models import *

import os


def alogin(request):
	response = HttpResponse()
	response.write({'username':'hello'})
#	response.write("<p> alogin </p>")
	return response

def alogout(request):
	response = HttpResponse()
	response.write("<p> alogout </p>")
	return response

def register(request):
	

	response = HttpResponse()
	response.write("<p> register </p>")
	return response

def uploadfile(request):
	response = HttpResponse()
	response.write("<p> uploadfile </p>")
	return response

def downloadfile(request):
	response = HttpResponse()
	response.write("<p> downloadfile </p>")
	return response

def search(request):
	response = HttpResponse()
	response.write("<p> search </p>")
	return response

