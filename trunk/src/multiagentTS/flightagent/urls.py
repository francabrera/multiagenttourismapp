'''
Created on 12/11/2010

@author: nicopernas
'''
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('flightagent.views',

#	('n', airportOrigen, airportDestino, fechaSalida, fechaRegreso, 'a', 'a', '1', 'e', '5')
	(r'^$', 'empty_url'),	
	(r'^(?P<airportOrigen>\w{3})/(?P<fechaSalida>\d{2}-\d{2}-\d{4})/to/(?P<airportDestino>\w{3})/(?P<fechaRegreso>\d{2}-\d{2}-\d{4})$', 'index'),

)
