from django import forms
from kk_module.models import *

class ModuleForm(forms.ModelForm):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = Module
        fields = ('id','project_workarea_id','module_name','module_due_date','module_estimatedtime','module_description',)

class ModuleUserForm(forms.ModelForm):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = ModuleUser
        fields = ('id','module_id','module_user',)
