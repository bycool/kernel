from django.conf.urls.defaults import *
from tvsite.tvshow.views import *

urlpatterns = patterns('',
		url(r'^success',success), 
		url(r'^register',register),
		url(r'^login',alogin),
		url(r'^logout',alogout),
		url(r'^upload_success',upload_file),
		url(r'^download_success',download_file),
		url(r'^play_video',play_video),
)
