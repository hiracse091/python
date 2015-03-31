from django.contrib import admin
from kk_task.models import Urgency, Task, TaskUser, TaskChecklist, ChecklistItem, TaskTime

# Register your models here.
admin.site.register(Urgency)
admin.site.register(Task)
admin.site.register(TaskUser)
admin.site.register(TaskChecklist)
admin.site.register(ChecklistItem)
admin.site.register(TaskTime)
