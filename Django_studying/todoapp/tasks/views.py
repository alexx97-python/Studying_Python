from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import TasksForm


def index(request):
    """
    This view allows us to add additional instances of Task class
    It also shows all instances that are already created
    """
    tasks = Task.objects.all()

    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/tasks/home/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/home.html', context)


def update_task(request, pk):
    """
    This view is used to update each instance of Task
    We get the instance of Task in a form that we can update and submit
    """
    task = Task.objects.get(id=pk)

    form = TasksForm(instance=task)

    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks/home/')
    context = {'form': form}

    return render(request, 'tasks/update_task.html', context)


def delete_task(request, pk):
    """
    This view is used to delete a specific instance of Task

    """
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/tasks/home/')

    context = {'item': item}

    return render(request, 'tasks/delete.html', context)
