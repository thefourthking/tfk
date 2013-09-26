# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from assignments.models import Assignment
from django.template import RequestContext, loader
import json
import requests

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
    response = requests.get("http://192.168.0.15:8000/results/1/result_123.json")
    json_data = json.loads(response.text)
    assignment = Assignment.objects.get(id = assignment_id)
    assignment.result = json_data['score']
    assignment.save()

    return HttpResponseRedirect("/assignments/1/results")

def results(request, assignment_id):
    assignment = Assignment.objects.get(id = assignment_id)
    template = loader.get_template('assignments/results.html')
    context = RequestContext(request, {
        'assignment': assignment,
    })
    return HttpResponse(template.render(context))

def solve(request, assignment_id):
    return HttpResponse("You're solving assignment %s." % assignment_id)
