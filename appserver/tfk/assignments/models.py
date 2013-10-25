import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.conf import settings

# Create your models here.
class Assignment(models.Model):
	start_date = models.DateTimeField('start date')
	end_date = models.DateTimeField('end date')
	question = models.CharField(max_length=500)
	result = models.CharField(max_length=100, default='new', editable=False)
	unittestfile = models.FileField(upload_to='.')

        def __unicode__(self):
                return self.question

@receiver(post_save, sender=Assignment)
def transmit_files(sender, **kwargs):
        assignment = kwargs['instance']

        print("The incoming unittest file gets copied to the sandbox VM")
        cmd = "scp -v -i %(ifile)s %(mediadir)s/%(filename)s %(appuser)s@%(sandbox)s:%(target_filename)s" % {
                "ifile": settings.APPCONFIG["identity_file"], 
                "mediadir": settings.MEDIA_ROOT,
                "filename": assignment.unittestfile,
                "appuser": settings.APPCONFIG["appuser"],
                "sandbox": settings.APPCONFIG["sandbox_vm"][0],
                "target_filename": "%s/lab_%sTest.java" % (settings.APPCONFIG['sandbox_base_dir'], assignment.pk)
        }
        print "WILL EXECUTE: %s" % cmd
        process = os.popen(cmd)
        print "OUTPUT: %s" % process.read()
