from django.template import loader, Context
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from tvsite.tvshow.models import *
#from tvsite.tvshow.views import *
# Create your views here.
import os

def register(request):
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
#				f=open('log.txt','a+')
#				f.write(str("success"))
#				f.close()
				auth.login(request,user)
				return HttpResponseRedirect('success')  
			else:  
				errors.append('disabled account') 
		else :  
			errors.append('invaild user')  
#	f=open('log.txt','w')
#	f.write(str("false"))
#	f.close()


	return render_to_response('login.html', {'errors': errors})

def alogout(request):  
	auth.logout(request)
	return HttpResponseRedirect('login')


def success(request):
#	username = request.COOKIES.get('username','')
	username = request.user.username
#	f=open('log.txt','w')
#	f.write(str(request.COOKIES.get('username')))
#	f.close()
	posts = UserFile.objects.all()
#	t = loader.get_template('upload_success.html')
#	c = Context({'posts':posts})
#	return HttpResponse(t.render(c))


	return render_to_response('success.html' ,{'username':username,'posts':posts})

def upload_file(request):
	if request.method == 'POST':
		u = request.user.username
		f = request.FILES['file']
		file_name = ""
		filename = ""
		try:
			pwd=os.getcwd()
			path = pwd + "/upload_file/" + u
			if not os.path.exists(path):
				os.makedirs(path)
			file_name = path + "/" + f.name
			destination = open(file_name, 'wb+')
			for chunk in f.chunks():
				destination.write(chunk)
			destination.close()
			UserFile.objects.create(Uername=u,filename=f.name,filepname=file_name)
			filename = f.name
		except Exception, e:
			print e
#		posts = UserFile.objects.all()
#		t = loader.get_template('upload_success.html')
#		c = Context({'posts':posts})
#		return HttpResponse(t.render(c))
		return render_to_response('upload_success.html' ,{'filename':filename})

from django.core.servers.basehttp import FileWrapper

def download_file(request):
	if request.method == 'POST':
		downloadfile = request.POST.get('downloadfile')
		#username = request.POST.get('username')


#		response = HttpResponse(read_file(downloadfile))
		filename = os.getcwd() + "/upload_file/" + request.user.username + "/" + downloadfile

#		response = HttpResponse(read_file(filename))
#		return response

#		f=open('log.txt','w')
#		f.write(str(downloadfile))
#		f.write(str(filename))
#		f.close()
		wrapper = FileWrapper(file(filename))
		response = HttpResponse(wrapper,content_type='text/plain')
		response['Content-Length'] = os.path.getsize(filename)
		response['Content-Encoding'] = 'utf-8'
		response['Content-Disposition'] = 'attachment;filename=%s' % filename
		return response
#	return render_to_response('upload_success.html' ,{'downloadfile':downloadfile})


def read_file(filename, buf_size=8192):
	f = open(filename, "rb")
	while True:
		content = f.read(buf_size)
		if content:
			yield content
		else:
			break

def play_video(request):
	playfile = request.POST.get('filename')
#	playfile = request.POST.get('playfile')
#	filepname = os.getcwd() + "/upload_file/" + request.user.username + "/" + playfile
	host = "http://192.168.7.97"
	filepname = host+"/ts/"+request.user.username+"/"+playfile
	#filepname = host+"/ts/"+request.user.username+"/"+playfile

	return render_to_response('play_video.html',{'playfile':playfile, 'filepname':filepname})
