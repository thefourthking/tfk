from django.contrib import admin
from assignments.models import Assignment
from assignments.models import Submission
from assignments.models import TfkSettings

admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(TfkSettings)
