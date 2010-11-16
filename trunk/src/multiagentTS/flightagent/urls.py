'''
Created on 12/11/2010

@author: nicopernas
'''
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('flightagent.views',

	(r'^$', 'index'),
	(r'^index$', 'index'),
)
