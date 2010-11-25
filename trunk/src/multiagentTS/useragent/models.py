'''
Created on 25/11/2010

@author: nicopernas
'''

from django.db import models

'''
''
'''
class CountryModels(models.Model):
    isocode = models.CharField(max_length = 2, primary_key = True)
    name = models.CharField(max_length = 50)
        
    def __unicode__(self):
        return self.name
    
    def getAirports(self):
        return self.airportmodels_set.all()
    
'''
''
'''        
class AirportModels(models.Model):
    iatacode = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    country = models.ForeignKey(CountryModels)
