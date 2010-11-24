'''
Created on 15/11/2010

@author: nicopernas
'''
from django.shortcuts import render_to_response
from django.template import RequestContext
from multiagentTS.flightagent.models import FlightModel
from multiagentTS.kayak import start_flight_search

def index(request):
	flightsearch = start_flight_search('n', 'MVD', 'TCI', '12/04/2010', '12/07/2010', 'a', 'a', '1', 'e', '10')
	if flightsearch is None:
		print "Mandar el error al template..."
	else:
		flights = []
		for f in flightsearch:
			flights.append(FlightModel(f))
			
		return render_to_response('flightagent_show_flights.html', {'flights': flights },
								context_instance = RequestContext(request))
