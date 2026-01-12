from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task


# Create your views here.
def addTask(request):
    task_var=(request.POST['task'])
    Task.objects.create(task=task_var )
    return redirect('home')
