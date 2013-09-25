# Create your views here.

from django.http import HttpResponse
from assignments.models import Assignment

def index(request):
    all_assignments = Assignment.objects.all()
    all_links = ""
    for a in all_assignments:
	all_links += "<a href=/assignments/%d> %s </a><br>" % (a.id, a.question)

    return HttpResponse(all_links)

def detail(request, assignment_id):
    return HttpResponse("Assignment title is: %s." % Assignment.objects.get(id = assignment_id))

def results(request, assignment_id):
    return HttpResponse("You're looking at the results of assignment %s." % assignment_id)

def solve(request, assignment_id):
    return HttpResponse("You're solving assignment %s." % assignment_id)
