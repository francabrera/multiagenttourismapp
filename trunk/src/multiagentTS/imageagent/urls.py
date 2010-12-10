
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('imageagent.views',
    (r'^(?P<pais_origen>[ \w]+)/(?P<ciudad_origen>[ \w]+)/to/(?P<pais_destino>[ \w]+)/(?P<ciudad_destino>[ \w]+)$', 'showImages'),
)
