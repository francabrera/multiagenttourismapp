'''
Created on 12/11/2010

@author: nicopernas
'''
from django import forms

# Create your models here.

class UserPreferencesForm(forms.Form):
	ciudadOrigen = forms.CharField(max_length = 100, required = True)
	ciudadDestino = forms.EmailField(max_length = 100, required = True)

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
