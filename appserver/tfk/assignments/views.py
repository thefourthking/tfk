# Create your views here.

import json
import requests

from django.http import HttpResponse, HttpResponseRedirect
from assignments.models import Assignment
from assignments.models import Submission 
from django.template import RequestContext, loader

from django.conf import settings

def index(request):
    if request.user.is_authenticated():
        print "logged in"

        all_submissions = Submission.objects.filter(user_id = request.user.id)
        all_assignments = Assignment.objects.all()
        template = loader.get_template('assignments/index.html')
        context = RequestContext(request, {
                'all_submissions': all_submissions,
                })
        
        return HttpResponse(template.render(context))
    else:
        return HttpResponse('Unauthorized', status=401)


def detail(request, assignment_id):
    assignment = Assignment.objects.get(id = assignment_id)

    template = loader.get_template('assignments/detail.html')
    context = RequestContext(request, {
        'assignment': assignment,
    })
    return HttpResponse(template.render(context))

def submit(request, assignment_id):
    assignment = Assignment.objects.get(id = assignment_id)
    assignment.result = 'solved'
    assignment.save()

    return HttpResponseRedirect("/assignments/%s/results" % assignment_id)

def results(request, assignment_id):
    assignment = Assignment.objects.get(id = assignment_id)

    if assignment.result == 'solved':
        try:
            results_url = "http://%s:8000/students/%s/results/%s.json" % (
                settings.APPCONFIG['sandbox_vm'][0], 
                settings.APPCONFIG['default_student_id'], 
                assignment_id)
            print "Will retrieve results like this: GET %s" % results_url
            response = requests.get(results_url)
            json_data = json.loads(response.text)
            print "Incoming JSON response: %s" % json_data
            assignment.result = "%s/%s" % (json_data['score'], json_data['total_tests'])
            assignment.save()
        except e:
            print "There was an error retrieving results"
            print e
            assignment.result = 'solved'
            assignment.save()
    
    template = loader.get_template('assignments/results.html')
    context = RequestContext(request, {
        'assignment': assignment,
    })
    return HttpResponse(template.render(context))

def solve(request, assignment_id):
    return HttpResponse("You're solving assignment %s." % assignment_id)
