from django.shortcuts import render
from .models import Project, Developer, Supervisor, Task
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Form_inscription, Form_supervisor, Form_project_create, Form_task_time
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def page(request):
    projects_list = Project.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(projects_list, 5)
    try:
        all_projects = paginator.page(page)
    except EmptyPage:
        all_projects = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        all_projects = paginator.page(1)
    return render(request, 'index.html', {'action': "Display all project", 'all_projects': all_projects})


def connection_page(request):
    return render(request, 'connection.html')


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    tasks = project.tasks.all()
    return render(request, 'project_detail.html', {'project': project, 'tasks': tasks})


def create_developer(request):
    error = False
    if request.POST:
        if 'name' in request.POST:
            name = request.POST.get('name', '')
        else:
            error = True
        if 'login' in request.POST:
            login = request.POST.get('login', '')
        else:
            error = True
        if 'password' in request.POST:
            password = request.POST.get('password', '')
        else:
            error = True
        if 'supervisor' in request.POST:
            supervisor_id = request.POST.get('supervisor', '')
        else:
            error = True
        if not error:
            supervisor = Supervisor.objects.get(id = supervisor_id)
            new_dev = Developer(name=name, login=login, password=password,
                                supervisor=supervisor)
            return HttpResponse("Developer added")
        else:
            return HttpResponse("An error has occured")
    else:
        supervisors_list = Supervisor.objects.all()

    return render(request, 'create_developer.html', {'supervisors_list': supervisors_list})


def create_project(request):
    if request.POST:
        form = Form_project_create(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            client_name = form.cleaned_data['client_name']
            new_project = Project(title=title, description=description, client_name=client_name)
            new_project.save()
            return HttpResponseRedirect(reverse('public_index'))
        else:
            return render(request, 'create_project.html', {'form': form })
    else:
        form = Form_project_create()
    return render(request, 'create_project.html', {'form': form})


def create_developer2(request):
    if request.POST:
        form = Form_inscription(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            supervisor = form.cleaned_data['supervisor']
            new_developer = Developer(name=name, login=login, password=password,
                                      email="",
                                      supervisor=supervisor)
            new_developer.save()
            return HttpResponse("Developer added")
        else:
            return render(request, 'create_developer2.html', {'form': form})
    else:
        form = Form_inscription(initial={'name': 'new', 'supervisor': Supervisor.objects.all().first()})
    return render(request, 'create_developer2.html', {'form': form})


class Developer_detail(DetailView):
    model = Developer
    template_name = 'developer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(Developer_detail, self).get_context_data(**kwargs)
        tasks_dev = Task.objects.filter(developer=self.object)
        context['tasks_dev'] = tasks_dev
        return context


class Task_update_time(UpdateView):
    model = Task
    template_name = 'update_task_developer.html'
    form_class = Form_task_time
    success_url = 'public_empty'

    def get_success_url(self):
        return reverse(self.success_url)

def public_empty(request):
    return HttpResponse("Successful operation!")


class Project_list(ListView):
    model = Project
    template_name = 'project_list2.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = Project.objects.all().order_by('title')
        return queryset


class Task_delete(DeleteView):
    model = Task
    template_name = 'confirm_delete_task.html'
    success_url = 'public_empty'

    def get_success_url(self):
        return reverse(self.success_url)

def create_supervisor(request):
    if request.POST:
        form = Form_supervisor(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('public_index'))
        else:
            return render(request, 'create_supervisor.html', {'form': form})
    else:
        form = Form_supervisor()
    return render(request, 'create_supervisor.html', {'form': form})