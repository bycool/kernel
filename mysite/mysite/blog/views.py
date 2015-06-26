from django.template import loader, Context
from django.http import HttpResponse
from mysite.blog.models import *
import os

def archive(request):
	posts = BlogPost.objects.all()
	t = loader.get_template("archive.html")
	c = Context({'posts':posts})
	return HttpResponse(t.render(c))

def login(request):
	posts = BlogPost.objects.all()
        t = loader.get_template("login.html")
        c = Context({'posts':posts})
        return HttpResponse(t.render(c))

from django.shortcuts import render_to_response

def upload_file(request):
	if request.method == 'POST':
#		f=open('log.txt','w')
#		f.write(str(request.method))
#		f.write(str(request.FILES['file']))
#		f.close()
		form = UploadFileForm(request.POST, request.FILES)
#		if form.is_valid():
		handle_uploaded_file(request.FILES['file'])
		posts = BlogPost.objects.all()
		t = loader.get_template("success.html")
		c = Context({'posts':posts})
		return HttpResponse(t.render(c))
	else:
		form = UploadFileForm()
	#return render_to_response('archive.html', {'form': form})
	return render_to_response('success.html', {'form': form})



def handle_uploaded_file(f):
	file_name = ""

	try:
#		path = "./" + time.strftime('/%Y/%m/%d/%H/%M/%S/')
		path = "/home/jiajiandong/test-django/mysite/"
		if not os.path.exists(path):
			os.makedirs(f)
		file_name = path + f.name
		destination = open(file_name, 'wb+')
		for chunk in f.chunks():
			destination.write(chunk)
		destination.close()
	except Exception, e:
		print e

	return file_name


# Create your views here.
