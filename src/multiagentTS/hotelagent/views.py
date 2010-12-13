'''
Created on 15/11/2010

@author: nicopernas
'''
from django.shortcuts import render_to_response
from django.template import RequestContext
from multiagentTS.hotelagent.models import HotelModel
from multiagentTS.kayak import start_hotel_search

def index(request, othercity, checkin_date, checkout_date):
    checkin_date = checkin_date.replace('-','/')
    checkout_date = checkout_date.replace('-','/')
    hotelsearch = start_hotel_search(othercity, checkin_date, checkout_date, '1', '1', '3', 'normal', 'down', 'price')

    hotels = []
    if hotelsearch is not None:
        for h in hotelsearch:
            hotels.append(HotelModel(h))
    return render_to_response('hotelagent_show_hotels.html', {'hotels': hotels },
                            context_instance = RequestContext(request))

def empty_url(request):
    
    html = ''' 
        <h3>Para realizar una b&uacute;squeda sobre un hotel, debe especificar:</h3>
        <ul>
            <li>Nombre de la ciudad y c&oacute;digo ISO del pa&iacute;s donde se va a hospedar, separados por una coma.</li>
            <li>Fecha de inicio de la estad&iacute;a con el formato MM/DD/AAAA.</li>
            <li>Fecha de finalizaci&oacute;n de la estad&iacute;a con el formato MM/DD/AAAA.</li>
        </ul>
        <span>Por ejemplo: http://servidor/hotel/Madrid,ES/12-20-2010/to/12-24-2010<span>
    '''
    return render_to_response('show_error_empty_url.html', {'message': html },
                        context_instance = RequestContext(request))