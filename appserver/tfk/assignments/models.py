from django.db import models

# Create your models here.
class Assignment(models.Model):
	start_date = models.DateTimeField('start date')
	end_date = models.DateTimeField('end date')
	question = models.CharField(max_length=500)
	result = models.CharField(max_length=100)

        def __unicode__(self):
                return self.question
