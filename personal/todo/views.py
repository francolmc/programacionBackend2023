from django.shortcuts import render
from django.views.generic import ListView
from todo.models import Task

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = "todo_task_list.html"
    context_object_name = "tasks"