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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'TasksManager.views.page', name="public_index"),
    url(r'^index$', 'TasksManager.views.page'),
    url(r'^connection$', 'TasksManager.views.connection_page', name="public_connection"),

    url(r'^project-detail-(?P<pk>\d+)$', 'TasksManager.views.project_detail', name="project_detail"),

    url(r'^create-developer$', 'TasksManager.views.create_developer', name="create_developer"),
    url(r'^add-developer$', 'TasksManager.views.create_developer2', name="add_developer"),
    url(r'^create-supervisor$', 'TasksManager.views.create_supervisor', name="create_supervisor"),
    url(r'^create-project$', 'TasksManager.views.create_project', name="create_project"),
]
