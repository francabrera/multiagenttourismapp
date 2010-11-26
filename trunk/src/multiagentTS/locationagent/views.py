# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.template import RequestContext

def showMap (request):
    
    pais_origen = request.GET['']
    pais_destino = request.GET['']
    ciudad_origen = request.GET['']
    ciudad_destino = request.GET['']
    
    flighturl = request.get_host() + 'flight/' + pais_origen + '/' + ciudad_origen + '/to/' + pais_destino + '/' + ciudad_destino
    context = {'flight_url': flighturl }
    return render_to_response('location.html', context)
