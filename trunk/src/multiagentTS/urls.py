from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^multiagentTS/', include('multiagentTS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^user/', include('useragent.urls')),
    (r'^location/', include('locationagent.urls')),
#   	(r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.USER_IMGS_ROOT, 'show_indexes': True}),
   	(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CSS_ROOT, 'show_indexes': True}),
   #	(r'^location/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/nicopernas/Documents/workspace/multiagentTS/src/multiagentTS/locationagent/templates', 'show_indexes': True}),
)
