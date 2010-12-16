'''
Created on 12/11/2010

@author: nicopernas
'''
from django import forms
from django.forms import ModelForm
from models import *

# Create your models here.

class UserPreferencesForm(forms.Form):
	paisOrigen = forms.CharField(max_length = 100, required = True)
	ciudadOrigen = forms.CharField(max_length = 100, required = True)
	paisDestino = forms.CharField(max_length = 100, required = True)
	ciudadDestino = forms.CharField(max_length = 100, required = True)
	fechaLlegada = forms.DateField(input_formats=['%d/%m/%Y'], required = True)
	fechaSalida = forms.DateField(input_formats=['%d/%m/%Y'], required = True)
	nPaisOrigen = forms.CharField(max_length = 100)
	nCiudadOrigen = forms.CharField(max_length = 100)
	nPaisDestino = forms.CharField(max_length = 100)
	nCiudadDestino = forms.CharField(max_length = 100)
	

	def clean_ciudadOrigen(self):
		ciudad = self.cleaned_data['ciudadOrigen']
		return ciudad

	def clean_ciudadDestino(self):
		ciudad = self.cleaned_data['ciudadDestino']
		return ciudad
	
	def clean_paisOrigen(self):
		pais = self.cleaned_data['paisOrigen']
		return pais

	def clean_paisDestino(self):
		pais = self.cleaned_data['paisDestino']
		return pais
	
	def clean_fechaLlegada(self):
		fecha = self.cleaned_data['fechaLlegada']
		return fecha

	def clean_fechaSalida(self):
		fecha = self.cleaned_data['fechaSalida']
		return fecha
	
	def nombreCiudadDestino (self):
		return self.cleaned_data['nCiudadDestino']
	
	def nombreCiudadOrigen (self):
		return self.cleaned_data['nCiudadOrigen']
	
	def nombrePaisDestino (self):
		return self.cleaned_data['nPaisDestino']
	
	def nombrePaisOrigen (self):
		return self.cleaned_data['nPaisOrigen']
	
class CountryForm(ModelForm):
	
	class Meta:
		model = CountryModels
		

class AirportForm(ModelForm):
	
	class Meta:
		model = AirportModels

