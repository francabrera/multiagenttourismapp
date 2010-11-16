'''
Created on 15/11/2010

@author: nicopernas
'''
import httplib, urllib
from xml.etree.ElementTree import ElementTree

# A Session ID (sid) is required before you can go any further in the API

# Each sid is good for 30 minutes
# Do not perform parallel searches against one sid. It will yield unpredictable results.
def getsession(token):
    hostname = "api.kayak.com"

    url = "http://" + hostname + "/k/ident/apisession?token=" + token
    feed = urllib.urlopen(url)
    tree = ElementTree()
    tree.parse(feed)
    sid = tree.find("sid")
    return sid.text


# oneway        | "y" or "n"
# origin        | v
# destination   | 3 letter airport code "BOS" "SFO" "DET"
# depart_date   | MM/DD/YY
# return_date   | MM/DD/YY

# depart_time   | "a" = any time; "r" = early am; "m" = am; "12" = noon; "n" = afternoon; "e" = evening; "l" = night;
# return_time   | ^
# travelers     | int 1-8

# cabin         | f, b, or e(default) (first, business, econ/coach)
def start_flight_search(sid, oneway, origin, destination, depart_date, return_date, depart_time, return_time, travelers, cabin):
    url = "/s/apisearch?basicmode=true&oneway=" + oneway + "&origin=" + origin + "&destination=" + destination + "&destcode=&depart_date=" + depart_date + "&depart_time=" + depart_time + "&return_date=" + return_date + "&return_time=" + return_time + "&travelers=" + travelers + "&cabin=" + cabin + "&action=doflights&apimode=1&_sid_=" + sid

    return start_search(url)

# othercity     | String locating the city. Should be City, RegionCode, CountryCode for US, Canada. Should be City, CountryCode for others
# checkin_date  | MM/DD/YYYY
# checkout_date | MM/DD/YYYY

# guests        | int 1-6
# rooms         | int 1-3
def start_hotel_search(sid, othercity, checkin_date, checkout_date, guests, rooms):
    url = "/s/apisearch?basicmode=true&othercity=" + othercity + "&checkin_date=" + checkin_date + "&checkout_date=" + checkout_date + "&guests1=" + guests + "&rooms=" + rooms + "&action=dohotels&apimode=1&_sid_=" + sid

    return start_search(url)

# this doesn't do anything useful yet
def start_search(url):
    print url
    searchid = ""
    return searchid

# http://www.kayak.com/labs/api/search/

def main():
    token = "z4tTR0X9aus5pyliwOZm0Q"
    sid = getsession(token)
    flightsearch = start_flight_search(sid, 'n', 'DTW', 'PTX', '11/08/2010', '11/20/2010', 'a', 'a', '1', 'e')

    hotelsearch = start_hotel_search(sid, 'Detroit, MI, US', '11/08/2010', '11/20/2010', '1', '1')

if __name__ == "__main__":
	main()
