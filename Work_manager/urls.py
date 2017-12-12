"""Work_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from TasksManager.models import Project, Task, Developer
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from TasksManager.views import Project_list, Developer_detail, Task_update_time, public_empty, Task_delete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'TasksManager.views.page', name="public_index"),
    url(r'^index$', 'TasksManager.views.page'),
    url(r'^public_connection$', 'TasksManager.views.connection_page', name="public_connection"),

    url(r'^project-detail-(?P<pk>\d+)$', 'TasksManager.views.project_detail', name="project_detail"),

    url(r'^create-developer$', 'TasksManager.views.create_developer', name="create_developer"),
    url(r'^add-developer$', 'TasksManager.views.create_developer2', name="add_developer"),
    url(r'^create-supervisor$', 'TasksManager.views.create_supervisor', name="create_supervisor"),
    # url(r'^create-project$', 'TasksManager.views.create_project', name="create_project"),


    # based on  CBV
    url(r'^create-project$', login_required(CreateView.as_view(model=Project, template_name='create_project.html',
                                               success_url='index', fields='__all__')), name="create_project"),
    url(r'^create-task$', CreateView.as_view(model=Task, template_name='create_task.html',
                                             success_url='index', fields='__all__'), name='create_task'),
    url(r'^project_list$', ListView.as_view(model=Project, template_name='project_list.html'), name='project_list'),
    url(r'^developer_list$', ListView.as_view(model=Developer, template_name='developer_list.html'),
        name='developer_list'),

    # url(r'^task_detail_(?P<pk>\d+)$', DetailView.as_view(model=Task, template_name='task_detail.html'),
        # name='task_detail'),
    url(r'^developer_detail_(?P<pk>\d+)$', Developer_detail.as_view(), name="developer_detail"),
    url(r'update_task_(?P<pk>\d+)$', UpdateView.as_view(model=Task, template_name='update_task.html',
                                                        success_url='index', fields='__all__'), name='update_task'),
    url(r'^update_task_time_(?P<pk>\d+)$', Task_update_time.as_view(), name='update_task_time'),
    url(r'task_delete_(?P<pk>\d+)$', Task_delete.as_view(), name='task_delete'),

    # custom CBV
    url(r'^project_list2$', Project_list.as_view(), name='project_list2'),

    url(r'update_result$', public_empty, name='public_empty'),

    # sessions
    url(r'^task_detail_(?P<pk>\d+)$', 'TasksManager.views.Task_detail', name='task_detail'),
    url(r'^task_list$', 'TasksManager.views.Task_list', name='task_list'),

    # login, logout
    url(r'^connection$', 'TasksManager.views.connection', name='connection'),
    url(r'^disconnect$', 'TasksManager.views.disconnect', name='disconnect'),
]
