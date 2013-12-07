from django.conf.urls import patterns, url
from assignments import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<assignment_id>\d+)/$', views.detail, name='detail'),
    # ex: /assignments/5/results/
    url(r'^submissions/(?P<submission_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<assignment_id>\d+)/submit/$', views.submit, name='submit'),
    # ex: /assignments/5/vote/
    url(r'^(?P<assignment_id>\d+)/solve/$', views.solve, name='solve'),
    url(r'^work$', views.work, name='work'),
)
