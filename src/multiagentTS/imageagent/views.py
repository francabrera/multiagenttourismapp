# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

def showImages (request, pais_origen, ciudad_origen, pais_destino, ciudad_destino):
    
    return render_to_response('image.html', {'destino': ciudad_destino})