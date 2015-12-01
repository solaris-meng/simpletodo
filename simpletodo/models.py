# encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

import time
import os

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User,null=True)
    upload_id = models.CharField(max_length=256, default='tmp')

    time_start = models.DateTimeField(null=True)
    time_end = models.DateTimeField(null=True)

    status = models.CharField(max_length=64, default='init')
    content = models.TextField(max_length=1024, default='tmp')

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.user.username

    def str_start(self):
        return self.time_start.strftime("%Y-%m-%d")
    def str_end(self):
        return self.time_end.strftime("%Y-%m-%d")


def update_filename(instance, filename):
    fpath = 'todo/' + time.strftime("%Y/%m/%d/")
    fname = instance.user.username + instance.upload_id + filename
    #fname = 'meng' + filename 
    return os.path.join(fpath, fname)

class TodoFile(models.Model):
    uploadfile = models.FileField(upload_to=update_filename)
    user = models.ForeignKey(User,null=True)
    upload_id = models.CharField(max_length=256, default='tmp')
    def __str__(self):
        return self.user.username
