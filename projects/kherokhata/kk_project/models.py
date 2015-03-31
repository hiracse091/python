from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_due_date = models.DateField(auto_now=False)
    project_estimatedtime = models.IntegerField()
    project_descriptoin = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.project_name

class WorkArea(models.Model):
    area = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.area

class ProjectDocument(models.Model):
    DOC_TYPE = (('1','original'),('2','new'))
    project_id = models.ForeignKey(Project)
    document_name = models.CharField(max_length=100)
    document_description = models.TextField()
    document_location = models.CharField(max_length=256)
    document_type = models.CharField(max_length=100, choices=DOC_TYPE)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.project_id.project_name + '-' + self.document_name

class ProjectUser(models.Model):
    project_id = models.ForeignKey(Project)
    project_user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.project_id.project_name + '-' + self.project_user.username

class ProjectWorkArea(models.Model):
    project_id = models.ForeignKey(Project)
    area_id = models.ForeignKey(WorkArea)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.project_id.project_name + '-' + self.area_id.area
    
    
