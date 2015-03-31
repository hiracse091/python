from django.db import models
from django.contrib.auth.models import User
from kk_project.models import ProjectWorkArea

# Create your models here.
class Module(models.Model):
    project_workarea_id = models.ForeignKey(ProjectWorkArea)
    module_name = models.CharField(max_length=100)
    module_due_date = models.DateField(auto_now=False)
    module_estimatedtime = models.IntegerField()
    module_description = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.project_workarea_id.project_id.project_name + '-' +  self.project_workarea_id.area_id.area + '-' + self.module_name

class ModuleUser(models.Model):
    module_id = models.ForeignKey(Module)
    module_user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.module_id.module_name + '-' + self.module_user.username
