'''
Created on 15/11/2010

@author: nicopernas
'''
from django.shortcuts import render_to_response
from django.template import RequestContext
from multiagentTS.flightagent.models import FlightModel
from multiagentTS.kayak import start_flight_search

def index(request, airportOrigen, fechaSalida, airportDestino, fechaRegreso):

	fechaSalida = fechaSalida.replace('-','/')
	fechaRegreso = fechaRegreso.replace('-','/')
	flightsearch = start_flight_search('n', airportOrigen, airportDestino, fechaSalida, fechaRegreso, 'a', 'a', '1', 'e', '5')

	flights = []
	if flightsearch is not None:
		for f in flightsearch:
			flights.append(FlightModel(f))
	return render_to_response('flightagent_show_flights.html', {'flights': flights },
					context_instance = RequestContext(request))


def empty_url(request):
	
	html = ''' 
		<h3>Para realizar una b&uacute;squeda sobre un vuelo debe especificar:</h3>
		<ul>
			<li>C&oacute;digo IATA del aeropuerto de salida.</li>
			<li>Fecha de salida con el formato MM/DD/AAAA.</li>
			<li>C&oacute;digo IATA del aeropuerto de llegada.</li>
			<li>Fecha de llegada con el formato MM/DD/AAAA.</li>				
		</ul>
		<span>Por ejemplo: http://servidor/flight/MAD/12-20-2010/to/JFK/12-24-2010</span>
	'''
	return render_to_response('show_error_empty_url.html', {'message': html },
						context_instance = RequestContext(request))