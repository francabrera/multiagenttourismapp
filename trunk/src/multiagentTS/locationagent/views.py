# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.template import RequestContext

def showMap (request, pais_origen, ciudad_origen, pais_destino, ciudad_destino): 
    fechaSalida = request.session['fecha_salida']
    sfechaSalida = fechaSalida.strftime('%m-%d-%Y')
    fechaLlegada = request.session['fecha_llegada']
    sfechaLlegada= fechaLlegada.strftime('%m-%d-%Y')
    nombrePaisDestino = request.session['pais_destino']
    nombrePaisOrigen = request.session['pais_origen']
    nombreCiudadDestino = request.session['ciudad_destino']
    nombreCiudadOrigen = request.session['ciudad_origen']
    
    flighturl = 'http://' + request.get_host() + '/flight/' + ciudad_origen + '/' + \
                sfechaSalida + '/to/' + ciudad_destino + '/' + sfechaLlegada
    imageurl = 'http://' + request.get_host() + '/image/' + nombrePaisOrigen + '/' + nombreCiudadOrigen + '/to/' + nombrePaisDestino + '/' + nombreCiudadDestino
    hotelurl = 'http://' + request.get_host() + '/hotel/' + nombreCiudadDestino + ',' + pais_destino + '/' + \
                sfechaSalida + '/to/' + sfechaLlegada
    guideurl = 'http://' + request.get_host() + '/guide/' + nombrePaisOrigen + '/' + nombreCiudadOrigen + '/to/' + nombrePaisDestino + '/' + nombreCiudadDestino
    
    context = {'flight_url': flighturl, 'image_url': imageurl,
               'hotel_url': hotelurl, 'guide_url': guideurl,
               'pais_origen': pais_origen, 'pais_destino': pais_destino,
               'ciudad_origen': ciudad_origen, 'ciudad_destino': ciudad_destino}
    
    return render_to_response('location.html', context)
