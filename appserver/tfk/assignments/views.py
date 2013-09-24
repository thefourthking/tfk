# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the assignments index.")

def detail(request, assignment_id):
    return HttpResponse("You're looking at assignment %s." % assignment_id)

def results(request, assignment_id):
    return HttpResponse("You're looking at the results of assignment %s." % assignment_id)

def solve(request, assignment_id):
    return HttpResponse("You're solving assignment %s." % assignment_id)
