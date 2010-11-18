from django.db import models

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
	airline		= models.CharField(max_length = 5)
	airlinename = models.CharField(max_length = 5)
	orig		= models.IntegerField()
	dest		= models.CharField(max_length = 50)
	depart		= models.DateField()
	arrive	 	= models.CharField(max_length = 50)
	stops		= models.DateField()
	durationmin	= models.CharField(max_length = 50)
	type		= models.CharField(max_length = 50)
	segments	= []
	

	def __init__(self, leg):
		models.Model.__init__(self)
		self.airline = leg.findtext('airline')
		self.airlinename = leg.findtext('airline_display')
		self.orig = leg.findtext('orig')
		self.dest = leg.findtext('dest')
		self.depart = leg.findtext('depart')
		self.arrive = leg.findtext('arrive')
		self.stops = leg.findtext('stops')
		self.duration_minutes = leg.findtext('duration_minutes')
		self.type = leg.findtext('cabin')
		segments = leg.findall('segment')
		for seg in segments:
			self.segments.append(SegmentModel(seg))

	def getSgments(self):
		return self.segments
	
'''
'' Clase que gestiona un vuelo
'''
class FlightModel(models.Model):
	price	= models.CharField(max_length = 50)
	ida		= LegModel
	vuelta	= LegModel

	def __init__(self, trip):
		models.Model.__init__(self)
		self.price	= trip.findtext('price')
		legs = trip.find('legs')
		self.ida = LegModel(legs[0])
		if legs[1] is not None:
			self.vuelta = LegModel(legs[1])
			
	def getIdaSegments(self):
		return self.ida.getSegments()
	
	def getVueltaSegments(self):
		return self.vuelta.getSegments()
	