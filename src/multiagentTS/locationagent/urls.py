'''
Created on 12/11/2010

@author: nicopernas
'''
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('locationagent.views',
	(r'^(?P<pais_origen>\w+)/(?P<ciudad_origen>\w+)/to/\
		(?P<pais_destino>\w+)/(?P<ciudad_destino>\w+)$', 'showMap'),
	#(r'^index$', 'showMap'),
)
