# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.template import RequestContext

def showMap (request, pais_origen, ciudad_origen, pais_destino, ciudad_destino): 
    fechaSalida = request.session['fecha_salida']
    sfechaSalida = fechaSalida.strftime('%m-%d-%Y')
    fechaLlegada = request.session['fecha_llegada']
    sfechaLlegada= fechaLlegada.strftime('%m-%d-%Y')
    flighturl = 'http://' + request.get_host() + '/flight/' + ciudad_origen + '/' + \
                sfechaSalida + '/to/' + ciudad_destino + '/' + sfechaLlegada
    imageurl = 'http://' + request.get_host() + '/image/' + pais_origen + '/' + ciudad_origen + '/to/' + pais_destino + '/' + ciudad_destino
    hotelurl = 'http://' + request.get_host() + '/image/' + pais_origen + '/' + ciudad_origen + '/to/' + pais_destino + '/' + ciudad_destino
    guideurl = 'http://' + request.get_host() + '/image/' + pais_origen + '/' + ciudad_origen + '/to/' + pais_destino + '/' + ciudad_destino
    context = {'flight_url': flighturl, 'image_url': imageurl,
               'hotel_url': hotelurl, 'guide_url': guideurl}
    return render_to_response('location.html', context)
