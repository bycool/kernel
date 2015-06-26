from django.conf.urls.defaults import *
from mysite.blog.views import *

urlpatterns = patterns('',
	url(r'^$',archive),
	url(r'login',login),
	url(r'success',upload_file)
)
