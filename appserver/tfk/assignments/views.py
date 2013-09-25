# Create your views here.

from django.http import HttpResponse
from assignments.models import Assignment
from django.template import RequestContext, loader

def index(request):
    all_assignments = Assignment.objects.all()
    template = loader.get_template('assignments/index.html')
    context = RequestContext(request, {
        'all_assignments': all_assignments,
    })

    return HttpResponse(template.render(context))

def detail(request, assignment_id):
    return HttpResponse("Assignment title is: %s." % Assignment.objects.get(id = assignment_id))

def results(request, assignment_id):
    return HttpResponse("You're looking at the results of assignment %s." % assignment_id)

def solve(request, assignment_id):
    return HttpResponse("You're solving assignment %s." % assignment_id)
