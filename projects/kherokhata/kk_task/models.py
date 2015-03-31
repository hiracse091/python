from django.db import models
from django.contrib.auth.models import User
from kk_module.models import Module

# Create your models here.
class Urgency(models.Model):
    urgency_level = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.urgency_level

class Task(models.Model):
    module_id = models.ForeignKey(Module)
    task_name = models.CharField(max_length=100)
    task_due_date = models.DateField(auto_now=False)
    #task_estimatedtime = models.IntegerField()
    task_description = models.TextField()
    task_urgency_level = models.ForeignKey(Urgency)
    TASK_TYPE = (('1','original'),('2','new'))
    task_type = models.CharField(max_length=100, choices=TASK_TYPE)
    TASK_STATUS = (('1','on'),('2','off'))
    task_status = models.CharField(max_length=100, choices=TASK_STATUS, default='2')
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.module_id.module_name + '-' + self.task_name

class TaskUser(models.Model):
    task_id = models.ForeignKey(Task)
    task_user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.task_id.task_name + '-' + self.task_user.username

class TaskChecklist(models.Model):
    task_id = models.ForeignKey(Task)
    task_checklist_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.task_id.task_name + '-' + self.task_checklist_name

class ChecklistItem(models.Model):
    checklist_id = models.ForeignKey(TaskChecklist)
    checklist_item = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.checklist_id.task_checklist_name + '-' + self.checklist_item

class TaskTime(models.Model):
    task_id = models.ForeignKey(Task)
    starttime = models.DateTimeField(auto_now_add=True)
    endtime = models.DateTimeField(auto_now=True)
    task_status = models.CharField(max_length=100, default='2')
    def __str__(self):
        return self.task_id.task_name



