# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

def showGuide (request, pais_origen, ciudad_origen, pais_destino, ciudad_destino):
    
    return render_to_response('guide.html', {'pais_origen': pais_origen,
                                             'pais_destino': pais_destino,
                                             'ciudad_origen': ciudad_origen,
                                             'ciudad_destino': ciudad_destino})