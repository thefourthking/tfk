# Create your views here.

import json
import requests

from django.http import HttpResponse, HttpResponseRedirect
from assignments.models import Assignment
from assignments.models import Submission 
from assignments.models import TfkSettings
from django.template import RequestContext, loader

from django.conf import settings

def index(request):
    if request.user.is_authenticated():
        print "logged in"

        all_assignments = Assignment.objects.all()
        all_submissions = Submission.objects.filter(user_id = request.user.id)
        template = loader.get_template('assignments/index.html')
        context = RequestContext(request, {
                'all_assignments': all_assignments,
                'all_submissions': all_submissions,
                })
        
        return HttpResponse(template.render(context))
    else:
        template = loader.get_template('assignments/landing.html')
        context = RequestContext(request)
        return HttpResponse(template.render(context))


def detail(request, assignment_id):
    tfk_settings = TfkSettings.objects.latest('pk')
    assignment = Assignment.objects.get(id = assignment_id)

    template = loader.get_template('assignments/detail.html')
    context = RequestContext(request, {
        'tfk_settings': tfk_settings,
        'assignment': assignment,
    })
    return HttpResponse(template.render(context))

def submit(request, assignment_id):
    submission = Submission(user_id_id=request.user.id, assignment_id_id=assignment_id)
    submission.result = 'solved'
    submission.save()

    return HttpResponseRedirect("/assignments/submissions/%s/results" % submission.id)

def results(request, submission_id):
    submission = Submission.objects.get(id = submission_id)
    assignment = submission.assignment_id

    if submission.result == 'solved':
        try:
            results_url = "http://%s:8000/students/%s/results/%s.json" % (
                settings.APPCONFIG['sandbox_vm'][0], 
                settings.APPCONFIG['default_student_id'], 
                assignment_id)
            print "Will retrieve results like this: GET %s" % results_url
            response = requests.get(results_url)
            json_data = json.loads(response.text)
            print "Incoming JSON response: %s" % json_data
            submission.result = "%s/%s" % (json_data['score'], json_data['total_tests'])
            submission.save()
        except:
            print "There was an error retrieving results"
            submission.result = 'solved'
            submission.save()
    
    template = loader.get_template('assignments/results.html')
    context = RequestContext(request, {
        'submission' : submission,
        'assignment': assignment,
    })
    return HttpResponse(template.render(context))

def solve(request, assignment_id):
    return HttpResponse("You're solving assignment %s." % assignment_id)
