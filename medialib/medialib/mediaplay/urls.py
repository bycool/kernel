from django.conf.urls.defaults import *
from medialib.mediaplay.views import *

urlpatterns = patterns('',
	url(r'^login',alogin),
	url(r'^logout',alogout),
	url(r'^register',register),
	url(r'^uploadfile',uploadfile),
	url(r'^downloadfile',downloadfile),
	url(r'^search',search),
)
