'''
Created on 26/11/2010

@author: nicopernas
'''

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import tostring
import re


import urllib

webserviceUrl = 'http://www.momondo.com/GeoWS.asmx/CompleteAirport?prefixText='
 
def getAirportLocation(airportCode):
    xmlresponse = urllib.urlopen(webserviceUrl + airportCode)
    if xmlresponse is None:
        return None
    else:
        parser = ElementTree()
        parser.parse(xmlresponse)
        str = tostring(parser.getroot())
        return re.sub('\<.*?\>', '', str)
