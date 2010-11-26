'''
Created on 26/11/2010

@author: nicopernas
'''

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import dump
import urllib

def getInfoFromAirportCode(url):
    xmlresponse = urllib.urlopen(url)
    if xmlresponse is None:
        return None
    else:
        parser = ElementTree()
        parser.parse(xmlresponse)
        dump(parser)