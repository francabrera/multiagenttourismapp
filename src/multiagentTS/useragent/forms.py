'''
Created on 12/11/2010

@author: nicopernas
'''
from django import forms
from django.forms import ModelForm
from models import *

# Create your models here.

class UserPreferencesForm(forms.Form):
	ciudadOrigen = forms.CharField(max_length = 100, required = True)
	ciudadDestino = forms.CharField(max_length = 100, required = True)

	def clean_ciudadOrigen(self):
		ciudad = self.cleaned_data['ciudadOrigen']
		if str.count(ciudad) == 0:
			raise forms.ValidationError("La ciudad de origen no puede ser vacia...")
		return ciudad

	def clean_ciudadDestino(self):
		ciudad = self.cleaned_data['ciudadDestino']
		if str.count(ciudad) == 0:
			raise forms.ValidationError("La ciudad de destino no puede ser vacia...")
		return ciudad
	
class CountryForm(ModelForm):
	
	class Meta:
		model = CountryModels
		

class AirportForm(ModelForm):
	
	class Meta:
		model = AirportModels

