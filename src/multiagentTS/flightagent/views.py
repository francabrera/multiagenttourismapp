'''
Created on 15/11/2010

@author: nicopernas
'''

import httplib, urllib
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import dump

from django.shortcuts import render_to_response
from multiagentTS.useragent.forms import UserPreferencesForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

hostname = "http://www.kayak.com"

def index(request):
	token = "z4tTR0X9aus5pyliwOZm0Q"
	sid = getsession(token)
	#print sid
	flightsearch = start_flight_search(sid, 'n', 'MVD', 'TCI', '12/04/2010', '12/07/2010', 'a', 'a', '1', 'e', '3')

	return render_to_response('flightagent_show_flights.html', {'flights': flightsearch },
								context_instance = RequestContext(request))

# this doesn't do anything useful yet
def start_search(sid, url, numres):
	xmlresponse = urllib.urlopen(url)
	parser = ElementTree()
	parser.parse(xmlresponse)
#	dump(parser)
	searchId = parser.findtext("searchid")
	url = hostname + "/s/basic/flight?searchid=" + searchId + "&c=" + numres + "&apimode=1" + "&_sid_=" + sid
#	print "La url es ", url
	xmlvuelos = urllib.urlopen(url)
	parser.parse(xmlvuelos)
	dump(parser)

	return parser

#http://www.kayak.com/s/basic/flight?searchid=SEARCHID&c=10&apimode=1&_sid_=SESSIONID
#http://www.kayak.com/s/basic       ?apimode=1&searchid=MaOdYK&c=10&amp;_sid_=30-Uqg010Rn1Qj1sC2fUxQ$
def getsession(token):
	url = hostname + "/k/ident/apisession?token=" + token
	feed = urllib.urlopen(url)
	tree = ElementTree()
	tree.parse(feed)
	#dump(tree)
	sid = tree.find("sid")
	return sid.text

def start_flight_search(sid, oneway, origin, destination, depart_date, return_date, depart_time, return_time, travelers, cabin, numres):
	url = hostname + "/s/apisearch?basicmode=true&oneway=" + oneway + "&origin=" + origin + "&destination=" + destination + "&destcode=&depart_date=" + depart_date + "&depart_time=" + depart_time + "&return_date=" + return_date + "&return_time=" + return_time + "&travelers=" + travelers + "&cabin=" + cabin + "&action=doFlights&apimode=1&_sid_=" + sid
	#print url
	return start_search(sid, url, numres)
