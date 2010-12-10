# Create your views here.
from django.shortcuts import render_to_response
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
			#cd = form.cleaned_data
			#send_mail(cd['subject'], cd['message'])
			return HttpResponseRedirect(showMap, 'A','B','C','D')
	else:
		form = UserPreferencesForm()
		form2 = UserPreferencesForm()
		countrymodels = CountryModels.objects.all()

		return render_to_response('initial_form.html', {'form': form, 'form2': form2,
								'countries': countrymodels},
								context_instance = RequestContext(request))

def thanks(request):
	return HttpResponse('Gracias!!!')
