
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('newsagent.views',

    (r'^$', 'index'),
    (r'^index$', 'index'),
)
