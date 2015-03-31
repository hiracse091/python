from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signin/$','kk_user.views.signin', name='signin'),
    url(r'^signout/$','kk_user.views.signout', name='signout'),

    url(r'^project/$','kk_user.views.project', name='project'),
    url(r'^project/details/$','kk_user.views.projectdetails', name='projectdetails'),
    url(r'^project/add/$','kk_user.views.add_project', name='add_project'),
    url(r'^project/edit/$','kk_user.views.edit_project', name='edit_project'),
    url(r'^project/delete/$','kk_user.views.delete_project', name='delete_project'),
    
    url(r'^workarea/$','kk_user.views.workarea', name='workarea'),
    url(r'^workarea/details/$','kk_user.views.workareadetails', name='workareadetails'),
    url(r'^workarea/add/$','kk_user.views.add_workarea', name='add_workarea'),
    url(r'^workarea/edit/$','kk_user.views.edit_workarea', name='edit_workarea'),
    url(r'^workarea/delete/$','kk_user.views.delete_workarea', name='delete_workarea'),

    url(r'^projectworkarea/$','kk_user.views.projectworkarea', name='projectworkarea'),
    url(r'^projectworkarea/details/$','kk_user.views.projectworkareadetails', name='projectworkareadetails'),
    url(r'^projectworkarea/add/$','kk_user.views.add_projectworkarea', name='add_projectworkarea'),
    url(r'^projectworkarea/edit/$','kk_user.views.edit_projectworkarea', name='edit_projectworkarea'),
    url(r'^projectworkarea/delete/$','kk_user.views.delete_projectworkarea', name='delete_projectworkarea'),

    url(r'^projectuser/$','kk_user.views.projectuser', name='projectuser'),
    url(r'^projectuser/details/$','kk_user.views.projectuserdetails', name='projectuserdetails'),
    url(r'^projectuser/add/$','kk_user.views.add_projectuser', name='add_projectuser'),
    url(r'^projectuser/edit/$','kk_user.views.edit_projectuser', name='edit_projectuser'),
    url(r'^projectuser/delete/$','kk_user.views.delete_projectuser', name='delete_projectuser'),

    url(r'^module/$','kk_user.views.module', name='module'),
    url(r'^module/details/$','kk_user.views.moduledetails', name='moduledetails'),
    url(r'^module/add/$','kk_user.views.add_module', name='add_module'),
    url(r'^module/edit/$','kk_user.views.edit_module', name='edit_module'),
    url(r'^module/delete/$','kk_user.views.delete_module', name='delete_module'),

    url(r'^moduleuser/$','kk_user.views.moduleuser', name='moduleuser'),
    url(r'^moduleuser/details/$','kk_user.views.moduleuserdetails', name='moduleuserdetails'),
    url(r'^moduleuser/add/$','kk_user.views.add_moduleuser', name='add_moduleuser'),
    url(r'^moduleuser/edit/$','kk_user.views.edit_moduleuser', name='edit_moduleuser'),
    url(r'^moduleuser/delete/$','kk_user.views.delete_moduleuser', name='delete_moduleuser'),

    url(r'^usertask/$','kk_user.views.usertask', name='usertask'),
    url(r'^usertask/details/$','kk_user.views.usertaskdetails', name='usertaskdetails'),
    url(r'^usertask/add/$','kk_user.views.add_usertask', name='add_usertask'),
    url(r'^usertask/edit/$','kk_user.views.edit_usertask', name='edit_usertask'),
    url(r'^usertask/delete/$','kk_user.views.delete_usertask', name='delete_usertask'),

    url(r'^urgency/$','kk_user.views.urgency', name='urgency'),
    url(r'^urgency/details/$','kk_user.views.urgencydetails', name='urgencydetails'),
    url(r'^urgency/add/$','kk_user.views.add_urgency', name='add_urgency'),
    url(r'^urgency/edit/$','kk_user.views.edit_urgency', name='edit_urgency'),
    url(r'^urgency/delete/$','kk_user.views.delete_urgency', name='delete_urgency'),

    url(r'^taskuser/$','kk_user.views.taskuser', name='taskuser'),
    url(r'^taskuser/details/$','kk_user.views.taskuserdetails', name='taskuserdetails'),
    url(r'^taskuser/add/$','kk_user.views.add_taskuser', name='add_taskuser'),
    url(r'^taskuser/edit/$','kk_user.views.edit_taskuser', name='edit_taskuser'),
    url(r'^taskuser/delete/$','kk_user.views.delete_taskuser', name='delete_taskuser'),

    url(r'^tasktime/$','kk_user.views.tasktime', name='tasktime'),
    url(r'^moduletime/$','kk_user.views.moduletime', name='moduletime'),
                       
    #routing for remote client
    url(r'^remotesignin/$','kk_user.views.remotesignin', name='remotesignin'),
    url(r'^profile/(?P<userid>[0-9]+)/$', 'kk_user.views.profile', name='profile'),
    url(r'^listmodules/$','kk_user.views.listmodules', name='listmodules'),
    url(r'^listtasks/$','kk_user.views.listtasks', name='listtasks'),
    url(r'^task/$','kk_user.views.task', name='task'),
    url(r'^task/start/$','kk_user.views.starttask', name='starttask'),
    url(r'^task/end/$','kk_user.views.endtask', name='endtask'),

    #routing for ajax calls
    url(r'^module/moduleuser/$','kk_user.views.populatemoduleuser', name='populatemoduleuser'),
    url(r'^task/taskuser/$','kk_user.views.populatetaskuser', name='populatetaskuser'),
    url(r'^module/estimatedtime/validate/$','kk_user.views.validateModuleEstimatedTime', name='validateModuleEstimatedTime'),
)   
