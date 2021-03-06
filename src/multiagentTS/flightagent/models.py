from django.db import models
from multiagentTS.funciones import getAirportLocation

# Create your models here.
'''
'' Clase que gestiona un tramo de un vuelo
'''

class SegmentModel(models.Model):
	airline		 = models.CharField(max_length = 5)
	flightnum	 = models.CharField(max_length = 5)
	durationmin	 = models.IntegerField()
	equip		 = models.CharField(max_length = 50)
	dtime		 = models.DateField()
	origaero	 = models.CharField(max_length = 50)
	atime		 = models.DateField()
	destaero	 = models.CharField(max_length = 50)
	type		 = models.CharField(max_length = 50)

	def __init__(self, segment):
		models.Model.__init__(self)
		self.airline = segment.findtext('airline')
		self.flightnum = segment.findtext('flight')
		self.durationmin = segment.findtext('duration_minutes')
		self.equip = segment.findtext('equip')
		self.dtime = segment.findtext('dt')
		self.origaero = segment.findtext('o')
		self.atime = segment.findtext('at')
		self.destaero = segment.findtext('d')
		self.type = segment.findtext('cabin')

'''
'' Clase que gestiona una ida o vuelta de un vuelo
'''
class LegModel(models.Model):
	orig		= models.CharField(max_length = 50)
	dest		= models.CharField(max_length = 50)
	depart		= models.DateField()
	arrive	 	= models.DateField()
	stops		= models.IntegerField()
	type		= models.CharField(max_length = 10)
	segments	= []
	ciudadO 	= models.CharField(max_length = 50)
	ciudadD 	= models.CharField(max_length = 50)
	

	def __init__(self, leg):
		models.Model.__init__(self)
		self.orig = leg.findtext('orig')
		self.dest = leg.findtext('dest')
		self.depart = leg.findtext('depart')
		self.arrive = leg.findtext('arrive')
		self.stops = leg.findtext('stops')
		self.type = leg.findtext('cabin')
		segments = leg.findall('segment')
		self.ciudadO = getAirportLocation(self.orig)
		self.ciudadD = getAirportLocation(self.dest)
		for seg in segments:
			self.segments.append(SegmentModel(seg))

	def getSgments(self):
		return self.segments
	
'''
'' Clase que gestiona un vuelo
'''
class FlightModel(models.Model):
	price	= models.CharField(max_length = 50)
	moneda	= models.CharField(max_length = 10)
	ida		= LegModel
	vuelta	= LegModel
	
	def __init__(self, trip):
		models.Model.__init__(self)
		self.price	= trip.findtext('price')
		self.moneda = trip.find('price').attrib['currency']
		legs = trip.find('legs')
		self.ida = LegModel(legs[0])
		if legs[1] is not None:
			self.vuelta = LegModel(legs[1])
			
			
	def getIdaSegments(self):
		return self.ida.getSegments()
	
	def getVueltaSegments(self):
		return self.vuelta.getSegments()
	