'''
Created on 12/11/2010

@author: nicopernas
'''
from django import forms

# Create your models here.

class UserPreferencesForm(forms.Form):
	ciudadOrigen = forms.CharField(max_length = 100, required = True)
	ciudadDestino = forms.EmailField(max_length = 100, required = True)
	message = forms.CharField(widget = forms.Textarea)

	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Not enough words!")
		return message
