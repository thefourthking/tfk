# Create your views here.

import json
import requests

from django.http import HttpResponse, HttpResponseRedirect
from assignments.models import Assignment
from django.template import RequestContext, loader

from django.conf import settings

def index(request):
    all_assignments = Assignment.objects.all()
    template = loader.get_template('assignments/index.html')
    context = RequestContext(request, {
        'all_assignments': all_assignments,
    })

    return HttpResponse(template.render(context))

def detail(request, assignment_id):
    assignment = Assignment.objects.get(id = assignment_id)

    template = loader.get_template('assignments/detail.html')
    context = RequestContext(request, {
        'assignment': assignment,
    })
    return HttpResponse(template.render(context))

def submit(request, assignment_id):
    results_url = "http://%s:8000/students/%s/results/%s.json" % (
        settings.APPCONFIG['sandbox_vm'][0], 
        settings.APPCONFIG['default_student_id'], 
        assignment_id)
    response = requests.get(results_url)
    json_data = json.loads(response.text)
    assignment = Assignment.objects.get(id = assignment_id)
    assignment.result = json_data['score']
    assignment.save()

    return HttpResponseRedirect("/assignments/%s/results" % assignment_id)

def results(request, assignment_id):
    assignment = Assignment.objects.get(id = assignment_id)
    template = loader.get_template('assignments/results.html')
    context = RequestContext(request, {
        'assignment': assignment,
    })
    return HttpResponse(template.render(context))

def solve(request, assignment_id):
    return HttpResponse("You're solving assignment %s." % assignment_id)
