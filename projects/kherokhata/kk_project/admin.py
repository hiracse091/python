from django.contrib import admin
from kk_project.models import Project, WorkArea, ProjectDocument, ProjectUser, ProjectWorkArea

# Register your models here.
admin.site.register(Project)
admin.site.register(WorkArea)
admin.site.register(ProjectDocument)
admin.site.register(ProjectUser)
admin.site.register(ProjectWorkArea)