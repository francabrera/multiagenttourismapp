# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

def showMap (request):
    context = {'coor_x': 28.488137,
               'coor_y': -16.31753,}
    return render_to_response('location.html', context)
