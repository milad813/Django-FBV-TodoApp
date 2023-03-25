from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'tasks/list_task.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        context['tasks'] = Task.objects.filter(user=self.request.user)
        return context

    
class CreateTaskView(LoginRequiredMixin,CreateView):
    form_class = TaskForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    success_url = '/'
    
    
'''
This view is Updated to Class based Views ov IndexView and CreateTaskView
@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
        return redirect("/")
    context = {"tasks": tasks, "form": form}
    return render(request, "tasks/list_task.html", context)
'''

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    fields=('title',)
    template_name = 'tasks/update_task.html'
    success_url = '/'
    def get_queryset(self):
        querry = Task.objects.filter(user=self.request.user)
        return querry
        
@login_required
def updateTask(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
            return redirect("/")

    context = {"form": form}

    return render(request, "tasks/update_task.html", context)


@login_required
def completeTask(request, pk):
    item = get_object_or_404(Task, id=pk, user=request.user)
    item.complete = True
    item.save()
    return redirect("/")


@login_required
def deleteTask(request, pk):
    item = get_object_or_404(Task, id=pk, user=request.user)
    item.delete()
    return redirect("/")
