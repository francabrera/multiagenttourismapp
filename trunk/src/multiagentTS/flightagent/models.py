from django.db import models

# Create your models here.

class FlightModel(models.Model):
	price = models.CharField()


	first_name = models.CharField(max_length = 50)
