from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def homepage(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    tasks = Task.objects.filter(
        Q(task_title__icontains=q) |
        Q(task_status__icontains=q)
    )
    context = {
        'tasks': tasks,
        'status': 'Completed',
    }

    return render(request, 'ToDoTask/index.html', context)


def newtask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_status = 'Not Completed'
            task.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'ToDoTask/new-task.html', context)


def complete(request, pk):
    task = Task.objects.get(id=pk)
    task.task_status = 'Completed'
    task.save()
    return redirect('home')


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'ToDoTask/delete.html', {'obj': task.task_title})
