from django.conf.urls.defaults import *
from tvsite.tvshow.views import *

urlpatterns = patterns('',
		url(r'^register',Useregist),
		url(r'^login',alogin),
		url(r'^logout',alogout),
)
