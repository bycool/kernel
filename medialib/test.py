#!/usr/bin/env python
#coding=utf8
 
import httplib,urllib
 
httpClient = None
 
try:
#	params = urllib.urlencode({'username':'','password':''})
#	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	httpClient = httplib.HTTPConnection('localhost', 8000, timeout=30)
#	httpClient.request('GET', '/tvshow/login')
	httpClient.request('GET', '/mediaplay/login') #mediaplay/login
 
	#response是HTTPResponse对象
	response = httpClient.getresponse()
	print response.status
	print response.reason #FOUND
	print response.read()

except Exception, e:
	print e
finally:
	if httpClient:
		httpClient.close()
