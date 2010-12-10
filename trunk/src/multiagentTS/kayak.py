'''
Created on 17/11/2010

@author: nicopernas
'''
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import dump
import urllib


hostname = 'http://www.kayak.com'
apisearch = '/s/apisearch?basicmode=true&apimode=1'

''' Funcion que obtiene un sid en kayak.com para poder realizar busquedas '''
def getsession():
    token = 'z4tTR0X9aus5pyliwOZm0Q'
    url = hostname + '/k/ident/apisession?token=' + token
    sid = getAndParseUrl(url)
    if sid is None:
        return None
    else:
        return sid.findtext('sid')
''' ----------------------------------------------------------------------- '''

''' Obtiene una respuesta en XML segun la url dada en kayak.com '''
def getAndParseUrl(url):
    xmlresponse = urllib.urlopen(url)
    if xmlresponse is None:
        return None
    else:
        parser = ElementTree()
        parser.parse(xmlresponse)
        return parser
''' ----------------------------------------------------------------------- '''

''' Funcion que obtiene vuelos consultando en kayak.com '''
def start_flight_search(oneway, origin, destination, depart_date, return_date, depart_time, return_time, travelers, cabin, numres):
    sid = getsession()
    if sid is None:
        raise Exception('No se pudo obtener identificador de sesion...')
    else:
        url = hostname + apisearch + '&oneway=' + oneway + '&origin=' + origin +'&destination=' + destination + '&destcode=' + '&depart_date=' + depart_date + '&depart_time=' + depart_time + '&return_date=' + return_date + '&return_time=' + return_time + '&travelers=' + travelers + '&cabin=' + cabin + '&action=doFlights' + '&_sid_=' + sid
        searchId = getAndParseUrl(url).findtext('searchid')
        if searchId is None:
            raise Exception('No se pudo obtener identificador de busqueda...')
        else:
            url = hostname + '/s/basic/flight?searchid=' + searchId + '&c=' + numres + '&apimode=1' + '&_sid_=' + sid
            parse = getAndParseUrl(url)
            if parse is None:
                raise Exception('No se pudo obtener resultados de busqueda...')
            else: 
                return parse.findall('trips/trip')
''' ----------------------------------------------------------------------- '''

''' Esta funcion obtiene hoteles consultando en kayak.com '''
def start_hotel_search(othercity, checkin_date, checkout_date, guests1, rooms, numres, mode, sortdir, sortkey):
    sid = getsession()
    if sid is None:
        raise Exception('No se pudo obtener identificador de sesion...')
    else:
        url = hostname + apisearch + '&othercity=' + othercity + '&checkin_date=' + checkin_date + '&checkout_date=' + checkout_date + '&guests1=' + guests1 + '&rooms=' + rooms + '&action=doHotels&version=1&_sid_=' + sid
        print url
        searchId = getAndParseUrl(url)
        dump(searchId)
        searchId = searchId.findtext('searchid')
        url = hostname + '/s/basic/hotel?searchid=' + searchId + '&c=' + numres + '&m='+ mode + '&d=' + sortdir + '&s=' + sortkey + '&apimode=1&version=1' + '&_sid_=' + sid
        parse = getAndParseUrl(url)
        if parse is None:
            return None
        else: 
            dump(parse)
            return parse.findall('hotels/hotel')
''' ----------------------------------------------------------------------- '''
