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
		num_words = len(ciudadOrigen)
		if num_words < 4:
			raise forms.ValidationError("Not enough words!")
		return message
