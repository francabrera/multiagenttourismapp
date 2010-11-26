'''
Created on 15/11/2010

@author: nicopernas
'''
from django.shortcuts import render_to_response
from django.template import RequestContext
from multiagentTS.flightagent.models import *
from multiagentTS.kayak import start_flight_search

def index(request):

	airportOrigen = 'TCI' #request
	airportDestino = 'MVD' #request
	fechaSalida = '01/04/2011' #request
	fechaRegreso = '01/15/2011' #request
	
	flightsearch = start_flight_search('n', airportOrigen, airportDestino, fechaSalida, fechaRegreso, 'a', 'a', '1', 'e', '5')

	if flightsearch is None:
		print "Mandar el error al template..."
	else:
		flights = []
		for f in flightsearch:
			flights.append(FlightModel(f))
	return render_to_response('flightagent_show_flights.html', {'flights': flights },
							context_instance = RequestContext(request))
