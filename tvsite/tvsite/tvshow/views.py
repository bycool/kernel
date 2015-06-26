from django.template import loader, Context
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
# Create your views here.

def Useregist(request):
	errors	= []
	username = None
	password = None
	email = None

	if request.method == 'POST':
		if not request.POST.get('username'):
			errors.append('please enter acount')
		else:
			username = request.POST.get('username')

		password = request.POST.get('password')
		email = request.POST.get('email')

	if username is not None and email is not None and password is not None:
		user = User.objects.create_user(username,email,password)
		return HttpResponseRedirect('login')

	return render_to_response('register.html', {'errors': errors})  

def alogin(request):  
	errors= [] 
	username = None  
	password = None  
	if request.method == 'POST' :
		username = request.POST.get('username') 
		password = request.POST.get('password')  
		user = authenticate(username=username,password=password)  
		if user is not None:  
			if user.is_active:
				auth.login(request,user)
				return HttpResponseRedirect('index')  
			else:  
				errors.append('disabled account') 
		else :  
			errors.append('invaild user')  

	return render_to_response('login.html', {'errors': errors})

def alogout(request):  
	auth.logout(request)
	return HttpResponseRedirect('')


def index(request):
#	username = request.COOKIES.get('username','')
	username = request.user.username
	f=open('log.txt','w')
	f.write(str(request.COOKIES.get('username')))
	f.close()

	return render_to_response('index.html' ,{'username':username})
