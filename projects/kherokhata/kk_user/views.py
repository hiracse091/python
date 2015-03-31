from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login, logout

from json import JSONEncoder

from django.contrib.auth.models import User
from kk_user.models import *
from kk_project.models import *
from kk_module.models import *
from kk_task.models import *

from datetime import timedelta
from datetime import datetime
from django.utils import timezone

from kk_project.forms import *
from kk_module.forms import *
from kk_task.forms import *

# Create your views here.

# ------------------------------------------------remote client views----------------------------------------------------
def remotesignin(request):
    if request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('kk_user:profile', args=(user.id,)))
        else:
            msg = JSONEncoder().encode({"result": "0"})
            return HttpResponse(msg)

def profile(request, userid):
    try:
        user = User.objects.get(id = userid)
        profile = UserProfile.objects.get(user=user)
        projects = ProjectUser.objects.filter(project_user=user)
        projectlist = []
        for project in projects:
            project_data = {}
            project_data['projectid'] = project.project_id.id
            project_data['projectname'] = project.project_id.project_name
            projectlist.append(project_data)
        user_profile = {"userid":user.id, "name":user.username, "emp_id":profile.emp_id, "email":profile.email, "projectlist":projectlist}
        msg = JSONEncoder().encode({"result": "1", "userprofile":user_profile})
        return HttpResponse(msg)
    except:
        msg = JSONEncoder().encode({"result":"0"})
        return HttpResponse(msg)

def listmodules(request):
    if request.method == 'GET':
        userid  = request.GET['userid']
        projectid = request.GET['projectid']
        try:
            user = User.objects.get(id = userid)
            project = Project.objects.get(id = projectid)
            project_workareas = ProjectWorkArea.objects.filter(project_id = project)
            list_project_workareas = []
            for project_workarea in project_workareas:
                list_project_workareas.append(project_workarea)
            list_modules = []
            for item in list_project_workareas:
                workarea_modules = Module.objects.filter(project_workarea_id = item)
                for i in workarea_modules:
                    list_modules.append(i)
            list_module_user = []
            for module in list_modules:
                try:
                    m = ModuleUser.objects.get(module_id = module, module_user = user)
                    list_module_user.append(m)
                except:
                    pass
            modulelist = []
            for module in list_module_user:
                module_data = {}
                module_data['moduleid'] = module.module_id.id
                module_data['modulename'] = module.module_id.module_name
                modulelist.append(module_data)
            user_module = {"modulelist":modulelist}
            msg = JSONEncoder().encode({"result": "1", "user_module":user_module})
            return HttpResponse(msg)
        except:
            msg = JSONEncoder().encode({"result":"0"})
            return HttpResponse(msg)

def listtasks(request):
    if request.method == 'GET':
        userid  = request.GET['userid']
        moduleid = request.GET['moduleid']
        try:
            user = User.objects.get(id = userid)
            module = Module.objects.get(id = moduleid)
            tasks = Task.objects.filter(module_id = module)
            list_task_user = []
            for task in tasks:
                try:
                    task_user = TaskUser.objects.get(task_id=task, task_user=user)
                    if task_user != None:
                        list_task_user.append(task_user)
                except:
                    pass
            tasklist = []
            for task in list_task_user:
                task_data = {}
                task_data['taskid'] = task.task_id.id
                task_data['taskname'] = task.task_id.task_name
                tasklist.append(task_data)
            user_task = {"tasklist":tasklist}
            msg = JSONEncoder().encode({"result": "1", "user_task":user_task})
            return HttpResponse(msg)
        except:
            msg = JSONEncoder().encode({"result":"0"})
            return HttpResponse(msg)

def task(request):
    if request.method == 'GET':
        userid  = request.GET['userid']
        taskid = request.GET['taskid']
        try:
            user = User.objects.get(id = userid)
            task = Task.objects.get(id = taskid)
            task_data = {}
            task_data['task_name'] = task.task_name
            task_data['task_due_date'] = str(task.task_due_date)
            #task_data['task_estimatedtime'] = str(task.task_estimatedtime)
            task_data['task_description'] = task.task_description
            task_data['task_urgency_level'] = task.task_urgency_level.urgency_level
            task_data['task_type'] = str(task.task_type)
            task_data['task_status'] = str(task.task_status)
            msg = JSONEncoder().encode({"result": "1", "task_data":task_data})
            return HttpResponse(msg)
        except:
            msg = JSONEncoder().encode({"result":"0"})
            return HttpResponse(msg)

def starttask(request):
    if request.method == 'GET':
        taskid = request.GET['taskid']
        try:
            task = Task.objects.get(id = taskid)
            task.task_status = '1'
            task.save()
            tasktime = TaskTime(task_id=task, task_status='1')
            tasktime.save()
            task_data = {}
            task_data['task_status'] = str(task.task_status)
            msg = JSONEncoder().encode({"result": "1", "task_data":task_data})
            return HttpResponse(msg)
        except:
            msg = JSONEncoder().encode({"result":"0"})
            return HttpResponse(msg)

def endtask(request):
    if request.method == 'GET':
        taskid = request.GET['taskid']
        try:
            task = Task.objects.get(id = taskid)
            task.task_status = '2'
            task.save()
            tasktimes = TaskTime.objects.get(task_id=task, task_status='1')
            tasktimes.task_status = '2'
            tasktimes.save()
            task_data = {}
            task_data['task_status'] = str(task.task_status)
            msg = JSONEncoder().encode({"result": "1", "task_data":task_data})
            return HttpResponse(msg)
        except:
            msg = JSONEncoder().encode({"result":"0"})
            return HttpResponse(msg)


# ------------------------------------------------web app views----------------------------------------------------
def home(request):
    return render(request, 'kk_user/login.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                profile = UserProfile.objects.get(user=user)
                msg =  {'user': user, 'profile':profile}
                return render(request, 'kk_user/index.html', msg)
            else:
                return render(request, 'kk_user/login.html')
        else:
            return render(request, 'kk_user/login.html')


def signout(request):
    logout(request)
    return render(request, 'kk_user/login.html')

def project(request):
    if request.method == 'GET':
        projects = []
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            if profile.user_type.id == 1:
                projects = Project.objects.all()
                msg =  {'user': user, 'profile':profile, 'projects': projects, 'projectcreate':'1'}
                return render(request, 'kk_user/index.html', msg)
            else:
                projectusers = ProjectUser.objects.filter(project_user=user)
                if len(projectusers) != 0:
                    for project in projectusers:
                        projects.append(project.project_id)
                    msg =  {'user': user, 'profile':profile, 'projects': projects, 'projectcreate':'1'}
                    return render(request, 'kk_user/index.html', msg)
                else:
                    msg =  {'user': user, 'profile':profile, 'projects': projects, 'projectcreate':'1'}
                    return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile, 'projects': projects, 'projectcreate':'1'}
            return render(request, 'kk_user/index.html', msg)

def projectdetails(request):
    if request.method == 'GET':
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            project = Project.objects.get(id = request.GET['projectid'])
            msg =  {'user': user, 'profile':profile, 'project': project}
            return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile}
            return render(request, 'kk_user/index.html', msg)

def workarea(request):
    if request.method == 'GET':
        workareas = []
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            workareas = WorkArea.objects.all()
            msg =  {'user': user, 'profile':profile, 'workareas': workareas, 'workareacreate':'1'}
            return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile, 'workareas': workareas, 'workareacreate':'1'}
            return render(request, 'kk_user/index.html', msg)

def workareadetails(request):
    if request.method == 'GET':
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            workarea = WorkArea.objects.get(id = request.GET['workareaid'])
            msg =  {'user': user, 'profile':profile, 'workarea': workarea}
            return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile}
            return render(request, 'kk_user/index.html', msg)

def projectworkarea(request):
    if request.method == 'GET':
        projectworkareas = []
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            if profile.user_type.id == 1:
                projectworkareas = ProjectWorkArea.objects.all()
                msg =  {'user': user, 'profile':profile, 'projectworkareas': projectworkareas, 'projectworkareacreate':'1'}
                return render(request, 'kk_user/index.html', msg)
            else:
                projectusers = ProjectUser.objects.filter(project_user=user)
                if len(projectusers) != 0:
                    for projectuser in projectusers:
                        workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                        for workarea in workareas:
                            projectworkareas.append(workarea)
                    msg =  {'user': user, 'profile':profile, 'projectworkareas': projectworkareas, 'projectworkareacreate':'1'}
                    return render(request, 'kk_user/index.html', msg)
                else:
                    msg =  {'user': user, 'profile':profile, 'projectworkareas': projectworkareas, 'projectworkareacreate':'1'}
                    return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile, 'projectworkareas': projectworkareas, 'projectworkareacreate':'1'}
            return render(request, 'kk_user/index.html', msg)

def projectworkareadetails(request):
    if request.method == 'GET':
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            projectworkarea = ProjectWorkArea.objects.get(id = request.GET['projectworkareaid'])
            msg =  {'user': user, 'profile':profile, 'projectworkarea': projectworkarea}
            return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile}
            return render(request, 'kk_user/index.html', msg)

def projectuser(request):
    if request.method == 'GET':
        projectusers = []
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            projectusers = ProjectUser.objects.all()
            msg =  {'user': user, 'profile':profile, 'projectusers': projectusers, 'projectusercreate':'1'}
            return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile, 'projectusers': projectusers, 'projectusercreate':'1'}
            return render(request, 'kk_user/index.html', msg)

def projectuserdetails(request):
    if request.method == 'GET':
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            projectuser = ProjectUser.objects.get(id = request.GET['projectuserdetailsid'])
            msg =  {'user': user, 'profile':profile, 'projectuser': projectuser}
            return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile}
            return render(request, 'kk_user/index.html', msg)

def module(request):
    if request.method == 'GET':
        modules = []
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            if profile.user_type.id == 1:
                modules = Module.objects.all()
                msg =  {'user': user, 'profile':profile, 'modules': modules, 'modulecreate':'1'}
                return render(request, 'kk_user/index.html', msg)
            elif profile.user_type.id == 2:
                projectusers = ProjectUser.objects.filter(project_user=user)
                if len(projectusers) != 0:
                    for projectuser in projectusers:
                        workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                        for workarea in workareas:
                            Modules = Module.objects.filter(project_workarea_id=workarea)
                            for module in Modules:
                                modules.append(module)
                    msg =  {'user': user, 'profile':profile, 'modules': modules, 'modulecreate':'1'}
                    return render(request, 'kk_user/index.html', msg)
                else:
                    msg =  {'user': user, 'profile':profile, 'modules': modules, 'modulecreate':'1'}
                    return render(request, 'kk_user/index.html', msg)
            else:
                moduleuserlist = ModuleUser.objects.filter(module_user=user)
                for item in moduleuserlist:
                    modules.append(item.module_id)
                msg =  {'user': user, 'profile':profile, 'modules': modules, 'modulecreate':'1'}
                return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile, 'modules': modules, 'modulecreate':'1'}
            return render(request, 'kk_user/index.html', msg)


def moduledetails(request):
    if request.method == 'GET':
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            module = Module.objects.get(id = request.GET['moduleid'])
            msg =  {'user': user, 'profile':profile, 'module': module}
            return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile}
            return render(request, 'kk_user/index.html', msg)

def moduleuser(request):
    if request.method == 'GET':
        moduleusers = []
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            if profile.user_type.id == 1:
                moduleusers = ModuleUser.objects.all()
                msg =  {'user': user, 'profile':profile, 'moduleusers': moduleusers, 'moduleusercreate':'1'}
                return render(request, 'kk_user/index.html', msg)
            else:
                projectusers = ProjectUser.objects.filter(project_user=user)
                if len(projectusers) != 0:
                    for projectuser in projectusers:
                        workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                        for workarea in workareas:
                            Modules = Module.objects.filter(project_workarea_id=workarea)
                            for module in Modules:
                                Moduleusers = ModuleUser.objects.filter(module_id=module)
                                for moduleuser in Moduleusers:
                                    moduleusers.append(moduleuser)
                    msg =  {'user': user, 'profile':profile, 'moduleusers': moduleusers, 'moduleusercreate':'1'}
                    return render(request, 'kk_user/index.html', msg)
                else:
                    msg =  {'user': user, 'profile':profile, 'moduleusers': moduleusers, 'moduleusercreate':'1'}
                    return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile, 'moduleusers': moduleusers, 'moduleusercreate':'1'}
            return render(request, 'kk_user/index.html', msg)


def moduleuserdetails(request):
    if request.method == 'GET':
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            moduleuser = ModuleUser.objects.get(id = request.GET['moduleuserid'])
            msg =  {'user': user, 'profile':profile, 'moduleuser': moduleuser}
            return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile}
            return render(request, 'kk_user/index.html', msg)
'''def usertask(request):
    if request.method == 'GET':
        tasks = []
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            if profile.user_type.id == 1:
                tasks = Task.objects.all()
                msg =  {'user': user, 'profile':profile, 'tasks': tasks}
                return render(request, 'kk_user/index.html', msg)
            else:
                projectusers = ProjectUser.objects.filter(project_user=user)
                if len(projectusers) != 0:
                    for projectuser in projectusers:
                        workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                        for workarea in workareas:
                            Modules = Module.objects.filter(project_workarea_id=workarea)
                            for module in Modules:
                                Tasks = Task.objects.filter(module_id=module)
                                for task in Tasks:
                                    tasks.append(task)
                    msg =  {'user': user, 'profile':profile, 'tasks': tasks}
                    return render(request, 'kk_user/index.html', msg)
                else:
                    msg =  {'user': user, 'profile':profile, 'tasks': tasks}
                    return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile, 'tasks': tasks}
            return render(request, 'kk_user/index.html', msg)'''

def usertask(request):
    if request.method == 'GET':
        tasks = []
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            if profile.user_type.id == 1:
                tasks = Task.objects.all()
                msg =  {'user': user, 'profile':profile, 'tasks': tasks, 'usertaskcreate':'1'}
                return render(request, 'kk_user/index.html', msg)
            elif profile.user_type.id == 2:
                projectusers = ProjectUser.objects.filter(project_user=user)
                if len(projectusers) != 0:
                    for projectuser in projectusers:
                        workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                        for workarea in workareas:
                            Modules = Module.objects.filter(project_workarea_id=workarea)
                            for module in Modules:
                                Tasks = Task.objects.filter(module_id=module)
                                for task in Tasks:
                                    tasks.append(task)
                    msg =  {'user': user, 'profile':profile, 'tasks': tasks, 'usertaskcreate':'1'}
                    return render(request, 'kk_user/index.html', msg)
                else:
                    msg =  {'user': user, 'profile':profile, 'tasks': tasks, 'usertaskcreate':'1'}
                    return render(request, 'kk_user/index.html', msg)
            else:
                taskuserlist = TaskUser.objects.filter(task_user=user)
                for item in taskuserlist:
                    tasks.append(item.task_id)
                msg =  {'user': user, 'profile':profile, 'tasks': tasks, 'usertaskcreate':'1'}
                return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile, 'tasks': tasks, 'usertaskcreate':'1'}
            return render(request, 'kk_user/index.html', msg)

def usertaskdetails(request):
    if request.method == 'GET':
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            task = Task.objects.get(id = request.GET['taskid'])
            msg =  {'user': user, 'profile':profile, 'task': task}
            return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile}
            return render(request, 'kk_user/index.html', msg)

def urgency(request):
    if request.method == 'GET':
        urgency = []
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            urgency = Urgency.objects.all()
            msg =  {'user': user, 'profile':profile, 'urgency': urgency, 'urgencycreate':'1'}
            return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile, 'urgency': urgency, 'urgencycreate':'1'}
            return render(request, 'kk_user/index.html', msg)

def urgencydetails(request):
    if request.method == 'GET':
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            urgencydetails = Urgency.objects.get(id = request.GET['urgencyid'])
            msg =  {'user': user, 'profile':profile, 'urgencydetails': urgencydetails}
            return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile}
            return render(request, 'kk_user/index.html', msg)

def taskuser(request):
    if request.method == 'GET':
        taskusers = []
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            if profile.user_type.id == 1:
                taskusers = TaskUser.objects.all()
                msg =  {'user': user, 'profile':profile, 'taskusers': taskusers, 'taskusercreate':'1'}
                return render(request, 'kk_user/index.html', msg)
            else:
                projectusers = ProjectUser.objects.filter(project_user=user)
                if len(projectusers) != 0:
                    for projectuser in projectusers:
                        workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                        for workarea in workareas:
                            Modules = Module.objects.filter(project_workarea_id=workarea)
                            for module in Modules:
                                Tasks = Task.objects.filter(module_id=module)
                                for task in Tasks:
                                    taskuserlist = TaskUser.objects.filter(task_id=task)
                                    for item in taskuserlist:
                                        taskusers.append(item)
                    msg =  {'user': user, 'profile':profile, 'taskusers': taskusers, 'taskusercreate':'1'}
                    return render(request, 'kk_user/index.html', msg)
                else:
                    msg =  {'user': user, 'profile':profile, 'taskusers': taskusers, 'taskusercreate':'1'}
                    return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile, 'taskusers': taskusers, 'taskusercreate':'1'}
            return render(request, 'kk_user/index.html', msg)

def taskuserdetails(request):
    if request.method == 'GET':
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            taskuser = TaskUser.objects.get(id = request.GET['taskuserid'])
            msg =  {'user': user, 'profile':profile, 'taskuser': taskuser}
            return render(request, 'kk_user/index.html', msg)
        except:
            msg =  {'user': user, 'profile':profile}
            return render(request, 'kk_user/index.html', msg)

#------------------------------------------------form views-------------------------------------------------
def add_project(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('kk_user:project'))
    else:
        form = ProjectForm()

    return render(request, 'kk_user/index.html', {'form': form, 'formtype': 'project', 'user': user, 'profile':profile})

def edit_project(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        project = Project.objects.get(id=request.POST['id'])
        editform = ProjectForm(request.POST, instance=project)
        if editform.is_valid():
            editform.save()
            return HttpResponseRedirect(reverse('kk_user:project'))
    else:
        project = Project.objects.get(id=request.GET['projectid'])
        editform = ProjectForm(instance=project)

    return render(request, 'kk_user/index.html', {'editform': editform, 'formtype': 'project', 'user': user, 'profile':profile})

def delete_project(request):
    if request.method == 'GET':
        try:
            project = Project.objects.get(id=request.GET['projectid'])
            project.delete()
            return HttpResponseRedirect(reverse('kk_user:project'))
        except:
            return HttpResponseRedirect(reverse('kk_user:project'))

def add_workarea(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = WorkAreaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('kk_user:workarea'))
    else:
        form = WorkAreaForm()

    return render(request, 'kk_user/index.html', {'form': form, 'formtype': 'workarea', 'user': user, 'profile':profile})

def edit_workarea(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        workarea = WorkArea.objects.get(id=request.POST['id'])
        editform = WorkAreaForm(request.POST, instance=workarea)
        if editform.is_valid():
            editform.save()
            return HttpResponseRedirect(reverse('kk_user:workarea'))
    else:
        workarea = WorkArea.objects.get(id=request.GET['workareaid'])
        editform = WorkAreaForm(instance=workarea)

    return render(request, 'kk_user/index.html', {'editform': editform, 'formtype': 'workarea', 'user': user, 'profile':profile})

def delete_workarea(request):
    if request.method == 'GET':
        try:
            workarea = WorkArea.objects.get(id=request.GET['workareaid'])
            workarea.delete()
            return HttpResponseRedirect(reverse('kk_user:workarea'))
        except:
            return HttpResponseRedirect(reverse('kk_user:workarea'))

def add_projectworkarea(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = ProjectWorkAreaForm(request.POST)
        projects = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for project in projectusers:
                    projects.append(project.project_id.id)
                form.fields["project_id"].queryset = Project.objects.filter(id__in=projects)
            except:
                pass
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('kk_user:projectworkarea'))
    else:
        form = ProjectWorkAreaForm()
        projects = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for project in projectusers:
                    projects.append(project.project_id.id)
                form.fields["project_id"].queryset = Project.objects.filter(id__in=projects)
            except:
                pass
    return render(request, 'kk_user/index.html', {'form': form, 'formtype': 'projectworkarea', 'user': user, 'profile':profile})

def edit_projectworkarea(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        projectworkarea = ProjectWorkArea.objects.get(id=request.POST['id'])
        editform = ProjectWorkAreaForm(request.POST, instance=projectworkarea)
        projects = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for project in projectusers:
                    projects.append(project.project_id.id)
                editform.fields["project_id"].queryset = Project.objects.filter(id__in=projects)
            except:
                pass
        if editform.is_valid():
            editform.save()
            return HttpResponseRedirect(reverse('kk_user:projectworkarea'))
    else:
        projectworkarea = ProjectWorkArea.objects.get(id=request.GET['projectworkareaid'])
        editform = ProjectWorkAreaForm(instance=projectworkarea)
        projects = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for project in projectusers:
                    projects.append(project.project_id.id)
                editform.fields["project_id"].queryset = Project.objects.filter(id__in=projects)
            except:
                pass

    return render(request, 'kk_user/index.html', {'editform': editform, 'formtype': 'projectworkarea', 'user': user, 'profile':profile})

def delete_projectworkarea(request):
    if request.method == 'GET':
        try:
            projectworkarea = ProjectWorkArea.objects.get(id=request.GET['projectworkareaid'])
            projectworkarea.delete()
            return HttpResponseRedirect(reverse('kk_user:projectworkarea'))
        except:
            return HttpResponseRedirect(reverse('kk_user:projectworkarea'))

def add_projectuser(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = ProjectUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('kk_user:projectuser'))
    else:
        form = ProjectUserForm()

    return render(request, 'kk_user/index.html', {'form': form, 'formtype': 'projectuser', 'user': user, 'profile':profile})

def edit_projectuser(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        projectuser = ProjectUser.objects.get(id=request.POST['id'])
        editform = ProjectUserForm(request.POST, instance=projectuser)
        if editform.is_valid():
            editform.save()
            return HttpResponseRedirect(reverse('kk_user:projectuser'))
    else:
        projectuser = ProjectUser.objects.get(id=request.GET['projectuserid'])
        editform = ProjectUserForm(instance=projectuser)

    return render(request, 'kk_user/index.html', {'editform': editform, 'formtype': 'projectuser', 'user': user, 'profile':profile})

def delete_projectuser(request):
    if request.method == 'GET':
        try:
            projectuser = ProjectUser.objects.get(id=request.GET['projectuserid'])
            projectuser.delete()
            return HttpResponseRedirect(reverse('kk_user:projectuser'))
        except:
            return HttpResponseRedirect(reverse('kk_user:projectuser'))

def add_module(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        projectworkareas = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                        workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                        for workarea in workareas:
                            projectworkareas.append(workarea.id)
                form.fields["project_workarea_id"].queryset = ProjectWorkArea.objects.filter(id__in=projectworkareas)
            except:
                pass
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('kk_user:module'))
    else:
        form = ModuleForm()
        projectworkareas = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                        workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                        for workarea in workareas:
                            projectworkareas.append(workarea.id)
                form.fields["project_workarea_id"].queryset = ProjectWorkArea.objects.filter(id__in=projectworkareas)
            except:
                pass
    return render(request, 'kk_user/index.html', {'form': form, 'formtype': 'module', 'user': user, 'profile':profile})

def edit_module(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        module = Module.objects.get(id=request.POST['id'])
        editform = ModuleForm(request.POST, instance=module)
        projectworkareas = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                        workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                        for workarea in workareas:
                            projectworkareas.append(workarea.id)
                editform.fields["project_workarea_id"].queryset = ProjectWorkArea.objects.filter(id__in=projectworkareas)
            except:
                pass
        if editform.is_valid():
            editform.save()
            return HttpResponseRedirect(reverse('kk_user:module'))
    else:
        module = Module.objects.get(id=request.GET['moduleid'])
        editform = ModuleForm(instance=module)
        projectworkareas = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                        workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                        for workarea in workareas:
                            projectworkareas.append(workarea.id)
                editform.fields["project_workarea_id"].queryset = ProjectWorkArea.objects.filter(id__in=projectworkareas)
            except:
                pass

    return render(request, 'kk_user/index.html', {'editform': editform, 'formtype': 'module', 'user': user, 'profile':profile})

def delete_module(request):
    if request.method == 'GET':
        try:
            module = Module.objects.get(id=request.GET['moduleid'])
            module.delete()
            return HttpResponseRedirect(reverse('kk_user:module'))
        except:
            return HttpResponseRedirect(reverse('kk_user:module'))

def add_moduleuser(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = ModuleUserForm(request.POST)
        modules = []
        users = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                    for workarea in workareas:
                        Modules = Module.objects.filter(project_workarea_id=workarea)
                        for module in Modules:
                            modules.append(module.id)   
                form.fields["module_id"].queryset = Module.objects.filter(id__in=modules)
            except:
                pass
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    projects = ProjectUser.objects.filter(project_id=projectuser.project_id)
                    for project in projects:
                        users.append(project.project_user.id)
                form.fields["module_user"].queryset = User.objects.filter(id__in=users)
            except:
                pass
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('kk_user:moduleuser'))
    else:
        form = ModuleUserForm()
        modules = []
        users = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                    for workarea in workareas:
                        Modules = Module.objects.filter(project_workarea_id=workarea)
                        for module in Modules:
                            modules.append(module.id)   
                form.fields["module_id"].queryset = Module.objects.filter(id__in=modules)
            except:
                pass
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    projects = ProjectUser.objects.filter(project_id=projectuser.project_id)
                    for project in projects:
                        users.append(project.project_user.id)
                form.fields["module_user"].queryset = User.objects.filter(id__in=users)
            except:
                pass

    return render(request, 'kk_user/index.html', {'form': form, 'formtype': 'moduleuser', 'user': user, 'profile':profile})

def edit_moduleuser(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        moduleuser = ModuleUser.objects.get(id=request.POST['id'])
        editform = ModuleUserForm(request.POST, instance=moduleuser)
        modules = []
        users = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                    for workarea in workareas:
                        Modules = Module.objects.filter(project_workarea_id=workarea)
                        for module in Modules:
                            modules.append(module.id)   
                editform.fields["module_id"].queryset = Module.objects.filter(id__in=modules)
            except:
                pass
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    projects = ProjectUser.objects.filter(project_id=projectuser.project_id)
                    for project in projects:
                        users.append(project.project_user.id)
                editform.fields["module_user"].queryset = User.objects.filter(id__in=users)
            except:
                pass
        if editform.is_valid():
            editform.save()
            return HttpResponseRedirect(reverse('kk_user:moduleuser'))
    else:
        moduleuser = ModuleUser.objects.get(id=request.GET['moduleuserid'])
        editform = ModuleUserForm(instance=moduleuser)
        modules = []
        users = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                    for workarea in workareas:
                        Modules = Module.objects.filter(project_workarea_id=workarea)
                        for module in Modules:
                            modules.append(module.id)   
                editform.fields["module_id"].queryset = Module.objects.filter(id__in=modules)
            except:
                pass
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    projects = ProjectUser.objects.filter(project_id=projectuser.project_id)
                    for project in projects:
                        users.append(project.project_user.id)
                editform.fields["module_user"].queryset = User.objects.filter(id__in=users)
            except:
                pass

    return render(request, 'kk_user/index.html', {'editform': editform, 'formtype': 'moduleuser', 'user': user, 'profile':profile})

def delete_moduleuser(request):
    if request.method == 'GET':
        try:
            moduleuser = ModuleUser.objects.get(id=request.GET['moduleuserid'])
            moduleuser.delete()
            return HttpResponseRedirect(reverse('kk_user:moduleuser'))
        except:
            return HttpResponseRedirect(reverse('kk_user:moduleuser'))

def add_usertask(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        modules = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                    for workarea in workareas:
                        Modules = Module.objects.filter(project_workarea_id=workarea)
                        for module in Modules:
                            modules.append(module.id)   
                form.fields["module_id"].queryset = Module.objects.filter(id__in=modules)
            except:
                pass
        if profile.user_type.id == 3:
            try:
                moduleusers = ModuleUser.objects.filter(module_user=user)
                #print moduleusers
                for moduleuser in moduleusers:
                    modules.append(moduleuser.module_id.id) 
                form.fields["module_id"].queryset = Module.objects.filter(id__in=modules)
            except:
                pass
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('kk_user:usertask'))
    else:
        form = TaskForm()
        modules = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                    for workarea in workareas:
                        Modules = Module.objects.filter(project_workarea_id=workarea)
                        for module in Modules:
                            modules.append(module.id)   
                form.fields["module_id"].queryset = Module.objects.filter(id__in=modules)
            except:
                pass
        if profile.user_type.id == 3:
            try:
                moduleusers = ModuleUser.objects.filter(module_user=user)
                #print moduleusers
                for moduleuser in moduleusers:
                    modules.append(moduleuser.module_id.id) 
                form.fields["module_id"].queryset = Module.objects.filter(id__in=modules)
            except:
                pass
    return render(request, 'kk_user/index.html', {'form': form, 'formtype': 'usertask', 'user': user, 'profile':profile})

def edit_usertask(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        usertask = Task.objects.get(id=request.POST['id'])
        editform = TaskForm(request.POST, instance=usertask)
        modules = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                    for workarea in workareas:
                        Modules = Module.objects.filter(project_workarea_id=workarea)
                        for module in Modules:
                            modules.append(module.id)   
                editform.fields["module_id"].queryset = Module.objects.filter(id__in=modules)
            except:
                pass
        if profile.user_type.id == 3:
            try:
                moduleusers = ModuleUser.objects.filter(module_user=user)
                #print moduleusers
                for moduleuser in moduleusers:
                    modules.append(moduleuser.module_id.id) 
                editform.fields["module_id"].queryset = Module.objects.filter(id__in=modules)
            except:
                pass
        if editform.is_valid():
            editform.save()
            return HttpResponseRedirect(reverse('kk_user:usertask'))
    else:
        usertask = Task.objects.get(id=request.GET['taskid'])
        editform = TaskForm(instance=usertask)
        modules = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                    for workarea in workareas:
                        Modules = Module.objects.filter(project_workarea_id=workarea)
                        for module in Modules:
                            modules.append(module.id)   
                editform.fields["module_id"].queryset = Module.objects.filter(id__in=modules)
            except:
                pass
        if profile.user_type.id == 3:
            try:
                moduleusers = ModuleUser.objects.filter(module_user=user)
                #print moduleusers
                for moduleuser in moduleusers:
                    modules.append(moduleuser.module_id.id) 
                editform.fields["module_id"].queryset = Module.objects.filter(id__in=modules)
            except:
                pass
    return render(request, 'kk_user/index.html', {'editform': editform, 'formtype': 'usertask', 'user': user, 'profile':profile})

def delete_usertask(request):
    if request.method == 'GET':
        try:
            usertask = Task.objects.get(id=request.GET['taskid'])
            usertask.delete()
            return HttpResponseRedirect(reverse('kk_user:usertask'))
        except:
            return HttpResponseRedirect(reverse('kk_user:usertask'))

def add_urgency(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = UrgencyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('kk_user:urgency'))
    else:
        form = UrgencyForm()

    return render(request, 'kk_user/index.html', {'form': form, 'formtype': 'urgency', 'user': user, 'profile':profile})

def edit_urgency(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        urgency = Urgency.objects.get(id=request.POST['id'])
        editform = UrgencyForm(request.POST, instance=urgency)
        if editform.is_valid():
            editform.save()
            return HttpResponseRedirect(reverse('kk_user:urgency'))
    else:
        urgency = Urgency.objects.get(id=request.GET['urgencyid'])
        editform = UrgencyForm(instance=urgency)

    return render(request, 'kk_user/index.html', {'editform': editform, 'formtype': 'urgency', 'user': user, 'profile':profile})

def delete_urgency(request):
    if request.method == 'GET':
        try:
            urgency = Urgency.objects.get(id=request.GET['urgencyid'])
            urgency.delete()
            return HttpResponseRedirect(reverse('kk_user:urgency'))
        except:
            return HttpResponseRedirect(reverse('kk_user:urgency'))

def add_taskuser(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = TaskUserForm(request.POST)
        tasks = []
        users = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                    for workarea in workareas:
                        Modules = Module.objects.filter(project_workarea_id=workarea)
                        for module in Modules:
                            Tasks = Task.objects.filter(module_id=module)
                            for task in Tasks:
                                tasks.append(task.id)
                form.fields["task_id"].queryset = Task.objects.filter(id__in=tasks)
            except:
                pass
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    projects = ProjectUser.objects.filter(project_id=projectuser.project_id)
                    for project in projects:
                        users.append(project.project_user.id)
                form.fields["task_user"].queryset = User.objects.filter(id__in=users)
            except:
                pass
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('kk_user:taskuser'))
    else:
        form = TaskUserForm()
        tasks = []
        users = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                    for workarea in workareas:
                        Modules = Module.objects.filter(project_workarea_id=workarea)
                        for module in Modules:
                            Tasks = Task.objects.filter(module_id=module)
                            for task in Tasks:
                                tasks.append(task.id)
                form.fields["task_id"].queryset = Task.objects.filter(id__in=tasks)
            except:
                pass
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    projects = ProjectUser.objects.filter(project_id=projectuser.project_id)
                    for project in projects:
                        users.append(project.project_user.id)
                form.fields["task_user"].queryset = User.objects.filter(id__in=users)
            except:
                pass

    return render(request, 'kk_user/index.html', {'form': form, 'formtype': 'taskuser', 'user': user, 'profile':profile})

def edit_taskuser(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        taskuser = TaskUser.objects.get(id=request.POST['id'])
        editform = TaskUserForm(request.POST, instance=taskuser)
        tasks = []
        users = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                    for workarea in workareas:
                        Modules = Module.objects.filter(project_workarea_id=workarea)
                        for module in Modules:
                            Tasks = Task.objects.filter(module_id=module)
                            for task in Tasks:
                                tasks.append(task.id)
                editform.fields["task_id"].queryset = Task.objects.filter(id__in=tasks)
            except:
                pass
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    projects = ProjectUser.objects.filter(project_id=projectuser.project_id)
                    for project in projects:
                        users.append(project.project_user.id)
                editform.fields["task_user"].queryset = User.objects.filter(id__in=users)
            except:
                pass
        if editform.is_valid():
            editform.save()
            return HttpResponseRedirect(reverse('kk_user:taskuser'))
    else:
        taskuser = TaskUser.objects.get(id=request.GET['taskuserid'])
        editform = TaskUserForm(instance=taskuser)
        tasks = []
        users = []
        if profile.user_type.id == 2:
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                    for workarea in workareas:
                        Modules = Module.objects.filter(project_workarea_id=workarea)
                        for module in Modules:
                            Tasks = Task.objects.filter(module_id=module)
                            for task in Tasks:
                                tasks.append(task.id)
                editform.fields["task_id"].queryset = Task.objects.filter(id__in=tasks)
            except:
                pass
            try:
                projectusers = ProjectUser.objects.filter(project_user=user)
                for projectuser in projectusers:
                    projects = ProjectUser.objects.filter(project_id=projectuser.project_id)
                    for project in projects:
                        users.append(project.project_user.id)
                editform.fields["task_user"].queryset = User.objects.filter(id__in=users)
            except:
                pass

    return render(request, 'kk_user/index.html', {'editform': editform, 'formtype': 'taskuser', 'user': user, 'profile':profile})


def delete_taskuser(request):
    if request.method == 'GET':
        try:
            taskuser = TaskUser.objects.get(id=request.GET['taskuserid'])
            taskuser.delete()
            return HttpResponseRedirect(reverse('kk_user:taskuser'))
        except:
            return HttpResponseRedirect(reverse('kk_user:taskuser'))

def tasktime(request):
    if request.method == 'GET':
        tasks = []
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            if profile.user_type.id == 1:
                tasks = Task.objects.all()
            elif profile.user_type.id == 2:
                projectusers = ProjectUser.objects.filter(project_user=user)
                if len(projectusers) != 0:
                    for projectuser in projectusers:
                        workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                        for workarea in workareas:
                            Modules = Module.objects.filter(project_workarea_id=workarea)
                            for module in Modules:
                                Tasks = Task.objects.filter(module_id=module)
                                for task in Tasks:
                                    tasks.append(task)        
            else:
                taskuserlist = TaskUser.objects.filter(task_user=user)
                for item in taskuserlist:
                    tasks.append(item.task_id)        
        except:
            pass
        taskdatalist = []
        for task in tasks:
            task_data = []
            task_data.append(task)
            tasktimes = TaskTime.objects.filter(task_id=task)
            timeelapsedtotal = timedelta(0, 0, 0)
            for tasktime in tasktimes:
                timeelapsed = tasktime.endtime - tasktime.starttime
                timeelapsedtotal += timeelapsed
            task_data.append(timeelapsedtotal)
            taskdatalist.append(task_data)
        msg =  {'user': user, 'profile':profile, 'taskdatalist':taskdatalist}
        return render(request, 'kk_user/index.html', msg)      

def moduletime(request):
    if request.method == 'GET':
        modules = []
        user = request.user
        profile = UserProfile.objects.get(user=user)
        try:
            if profile.user_type.id == 1:
                modules = Module.objects.all()
            elif profile.user_type.id == 2:
                projectusers = ProjectUser.objects.filter(project_user=user)
                if len(projectusers) != 0:
                    for projectuser in projectusers:
                        workareas = ProjectWorkArea.objects.filter(project_id=projectuser.project_id)
                        for workarea in workareas:
                            Modules = Module.objects.filter(project_workarea_id=workarea)
                            for module in Modules:
                                modules.append(module)
            else:
                moduleuserlist = ModuleUser.objects.filter(module_user=user)
                for item in moduleuserlist:
                    modules.append(item.module_id)        
        except:
            pass
        moduledatalist = []
        for module in modules:
            module_data = []
            module_data.append(module)
            tasks = Task.objects.filter(module_id=module)
            moduletimeelapsedtotal = timedelta(0, 0, 0)
            for task in tasks:
                tasktimes = TaskTime.objects.filter(task_id=task)
                timeelapsedtotal = timedelta(0, 0, 0)
                for tasktime in tasktimes:
                    timeelapsed = tasktime.endtime - tasktime.starttime
                    timeelapsedtotal += timeelapsed
                moduletimeelapsedtotal += timeelapsedtotal
            module_data.append(moduletimeelapsedtotal)
            moduledatalist.append(module_data)
        msg =  {'user': user, 'profile':profile, 'moduledatalist':moduledatalist}
        return render(request, 'kk_user/index.html', msg)

#--------------------------------------------------ajax views--------------------------------------

def populatemoduleuser(request):
    if request.method == 'GET':
        users = []
        try:
            module = Module.objects.get(id = request.GET['moduleid'])
            project = module.project_workarea_id.project_id
            projectusers = ProjectUser.objects.filter(project_id=project)
            for projectuser in projectusers:
                users.append(projectuser.project_user.id)
            userlist = User.objects.filter(id__in=users)
            
            user_data_list = []
            for item in userlist:
                user_data = {}
                user_data['userid'] = item.id
                user_data['username'] = item.username
                user_data_list.append(user_data)
            
            msg = JSONEncoder().encode({"moduleusers": user_data_list, "result": "success"})
            return HttpResponse(msg)
        except:
            msg = JSONEncoder().encode({"result": "error"})
            return HttpResponse(msg)

def populatetaskuser(request):
    if request.method == 'GET':
        users = []
        try:
            task = Task.objects.get(id = request.GET['taskid'])
            module = task.module_id
            moduleusers = ModuleUser.objects.filter(module_id=module)
            for moduleuser in moduleusers:
                users.append(moduleuser.module_user.id)
            userlist = User.objects.filter(id__in=users)
            
            user_data_list = []
            for item in userlist:
                user_data = {}
                user_data['userid'] = item.id
                user_data['username'] = item.username
                user_data_list.append(user_data)
            
            msg = JSONEncoder().encode({"taskusers": user_data_list, "result": "success"})
            return HttpResponse(msg)
        except:
            msg = JSONEncoder().encode({"result": "error"})
            return HttpResponse(msg)

def validateModuleEstimatedTime(request):
    if request.method == 'GET':
        try:
            project_workarea_id = request.GET['project_workarea_id']
            module_estimated_time= request.GET['module_estimated_time']
            projectworkarea = ProjectWorkArea.objects.get(id=project_workarea_id)
            project_estimated_time = projectworkarea.project_id.project_estimatedtime
            workareas = ProjectWorkArea.objects.filter(project_id=projectworkarea.project_id)
            modules = []
            for workarea in workareas:
                Modules = Module.objects.filter(project_workarea_id=workarea)
                for module in Modules:
                    modules.append(module)
            module_estimated_time_total = 0
            for module in modules:
                module_estimated_time_total += module.module_estimatedtime
            available_module_time = project_estimated_time - module_estimated_time_total
            if(int(module_estimated_time) > int(available_module_time)):
                msg = JSONEncoder().encode({"valid":"0", "available_module_time":available_module_time, "result": "success"})
                return HttpResponse(msg)
            else:
                msg = JSONEncoder().encode({"valid":"1", "available_module_time":available_module_time, "result": "success"})
                return HttpResponse(msg)
        except:
            msg = JSONEncoder().encode({"result": "error"})
            return HttpResponse(msg)
