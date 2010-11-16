# Create your views here.
from django.shortcuts import render_to_response
from multiagentTS.useragent.forms import UserPreferencesForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

def index(request):
	if request.method == 'POST':
		form = UserPreferencesForm(request.POST)
		if form.is_valid():
			#cd = form.cleaned_data
			#send_mail(cd['subject'], cd['message'])
			return HttpResponseRedirect('thanks/')
	else:
		form = UserPreferencesForm()
		return render_to_response('useragent_initial_form.html', {'form': form},
								context_instance = RequestContext(request))

def thanks(request):
	return HttpResponse('Gracias!!!')
