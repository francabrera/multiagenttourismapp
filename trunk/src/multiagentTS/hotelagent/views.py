'''
Created on 15/11/2010

@author: nicopernas
'''
from django.shortcuts import render_to_response
from django.template import RequestContext
from multiagentTS.hotelagent.models import HotelModel
from multiagentTS.kayak import start_hotel_search

def index(request):
    othercity = 'Montevideo,UY'
    checkin_date = '01/15/2011'
    checkout_date = '01/25/2011'
    guests1 = '1'
    rooms = '1'

    hotelsearch = start_hotel_search(othercity, checkin_date, checkout_date, guests1, rooms, '3', 'normal', 'down', 'price')

    if hotelsearch is None:
        raise  Exception("Mandar el error al template...")        #render_to_response('error_flight.html', {}, context_instance = RequestContext(request))
    else:
        hotels = []
        for h in hotelsearch:
            hotels.append(HotelModel(h))
    return render_to_response('hotelagent_show_hotels.html', {'hotels': hotels },
                            context_instance = RequestContext(request))
