from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tfk.views.home', name='home'),
    # url(r'^tfk/', include('tfk.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^assignments/', include('assignments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', lambda r : HttpResponseRedirect('assignments/')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'assignments/landing.html'}),
)
