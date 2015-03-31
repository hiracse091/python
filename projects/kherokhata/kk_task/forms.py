from django import forms
from kk_task.models import *

class TaskForm(forms.ModelForm):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = Task
        fields = ('id','module_id','task_name','task_due_date','task_description','task_urgency_level','task_type','task_status',)

class UrgencyForm(forms.ModelForm):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = Urgency
        fields = ('id','urgency_level',)

class TaskUserForm(forms.ModelForm):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = TaskUser
        fields = ('id','task_id','task_user',)
