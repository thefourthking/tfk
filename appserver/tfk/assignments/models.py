import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Assignment(models.Model):
	start_date = models.DateTimeField('start date')
	end_date = models.DateTimeField('end date')
	question = models.CharField(max_length=500)
	unittestfile = models.FileField(upload_to='.')

        def __unicode__(self):
                return self.question


class Submission(models.Model):
    assignment_id = models.ForeignKey(Assignment)
    user_id = models.ForeignKey(User)
    result = models.CharField(max_length=100, default='new')


class TfkSettings(models.Model):
    websockets_proxy_host = models.CharField(max_length=100, default='localhost')
    websockets_proxy_port = models.CharField(max_length=100, default='6080')
    vnc_password =   models.CharField(max_length=100, default='tfkpassword')
    ifile = models.FileField(upload_to='.')
    sandbox_host = models.CharField(max_length=100, default='localhost')
    sandbox_user =  models.CharField(max_length=100, default='tfk')
    sandbox_base_dir = models.CharField(max_length=100, default='/opt/fourthking/unit_tests')

@receiver(post_save, sender=Assignment)
def transmit_files(sender, **kwargs):
        tfk_settings = TfkSettings.objects.latest("id")
        assignment = kwargs['instance']

        print("The incoming unittest file gets copied to the sandbox VM")
        cmd = "scp -v -o StrictHostKeyChecking=no -i %(mediadir)s/%(ifile)s %(mediadir)s/%(filename)s %(appuser)s@%(sandbox)s:%(target_filename)s" % {
                "ifile": tfk_settings.ifile,
                "mediadir": settings.MEDIA_ROOT,
                "filename": assignment.unittestfile,
                "appuser": tfk_settings.sandbox_user,
                "sandbox": tfk_settings.sandbox_host,
                "target_filename": "%s/lab_%sTest.java" % (tfk_settings.sandbox_base_dir, assignment.pk)
        }
        print "WILL EXECUTE: %s" % cmd
        process = os.popen(cmd)
        print "OUTPUT: %s" % process.read()



