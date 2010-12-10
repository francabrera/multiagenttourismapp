# Create your views here.
from django.shortcuts import render_to_response, redirect
from multiagentTS.useragent.forms import *
from multiagentTS.locationagent.views import showMap
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from multiagentTS.useragent.models import CountryModels
from django.forms.models import inlineformset_factory

def index(request):
	FriendshipFormSet = inlineformset_factory(CountryModels, AirportModels)
	if request.method == 'POST':
		#form = UserPreferencesForm(request.POST)
		form2 = UserPreferencesForm(request.POST)
		if form2.is_valid():
			#send_mail(cd['subject'], cd['message'])
			return showMap(request, ciudad_origen = form2.clean_ciudadOrigen(),
						 ciudad_destino = form2.clean_ciudadDestino(),
						pais_origen = 'pais1',
						pais_destino = 'pais2')

		#return render_to_response('location', {})
	else:
		form2 = UserPreferencesForm()
		countrymodels = CountryModels.objects.all()

		return render_to_response('initial_form.html', {'form2': form2,
								'countries': countrymodels},
								context_instance = RequestContext(request))

def thanks(request):
	return HttpResponse('Gracias!!!')
