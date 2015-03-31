from django import forms
from kk_project.models import *

class ProjectForm(forms.ModelForm):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = Project
        fields = ('id','project_name','project_due_date','project_estimatedtime','project_descriptoin',)

class WorkAreaForm(forms.ModelForm):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = WorkArea
        fields = ('id','area',)

class ProjectWorkAreaForm(forms.ModelForm):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = ProjectWorkArea
        fields = ('id','project_id','area_id',)

class ProjectUserForm(forms.ModelForm):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = ProjectUser
        fields = ('id','project_id','project_user',)
