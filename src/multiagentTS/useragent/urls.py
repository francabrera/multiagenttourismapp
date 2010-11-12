'''
Created on 12/11/2010

@author: nicopernas
'''
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('useragent.views',

	(r'^$', 'index'),
	(r'^index$', 'index'),
	(r'^thanks$', 'thanks'),
#	(r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.USER_IMGS_ROOT, 'show_indexes': True}),
#   	(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.USER_CSS_ROOT, 'show_indexes': True}),
)
