'''
Created on 15/11/2010

@author: nicopernas
'''
from django.shortcuts import render_to_response
from django.template import RequestContext
from multiagentTS.flightagent.models import FlightModel
from multiagentTS.kayak import start_flight_search

def index(request, airportOrigen, fechaSalida, airportDestino, fechaRegreso):

	flightsearch = start_flight_search('n', airportOrigen, airportDestino, fechaSalida.replace('-','/'), fechaRegreso.replace('-','/'), 'a', 'a', '1', 'e', '5')

	if flightsearch is None:
		raise  Exception("Mandar el error al template...")		#render_to_response('error_flight.html', {}, context_instance = RequestContext(request))
	else:
		flights = []
		for f in flightsearch:
			flights.append(FlightModel(f))
	return render_to_response('flightagent_show_flights.html', {'flights': flights },
							context_instance = RequestContext(request))
