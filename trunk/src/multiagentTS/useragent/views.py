# Create your views here.
from django.shortcuts import render_to_response
from multiagentTS.useragent.forms import UserPreferencesForm
from multiagentTS.locationagent.views import showMap
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from multiagentTS.useragent.models import CountryModels

def index(request):
	if request.method == 'POST':
		form = UserPreferencesForm(request.POST)
		if form.is_valid():
			#cd = form.cleaned_data
			#send_mail(cd['subject'], cd['message'])
			return HttpResponseRedirect(showMap, 'A','B','C','D')
	else:
		form = UserPreferencesForm()
		countrymodels = CountryModels.objects.all()

		return render_to_response('initial_form.html', {'form': form, 'countries': countrymodels},
								context_instance = RequestContext(request))

def thanks(request):
	return HttpResponse('Gracias!!!')
