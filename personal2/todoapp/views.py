from django.shortcuts import render
# Aqui importamos las clases base que seran heredadas en cada una de las vistas
# Cada clase representa el comportamiento que necesitamos
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Aqui importamos la tabla Task que usaremos para mostrar, agregar, editar
# y eliminar tareas.
from todoapp.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class TaskListView(LoginRequiredMixin, ListView): # Esta es la vista que mostrara las tareas
    login_required = True
    model = Task # Aqui especificamos la tabla
    template_name = "todo_task_list.html" # Aqui especificamos el html que mostrara las tareas
    context_object_name = "tasks" # Aqui especificamos el nombre 
    # que daremos la variable que mostrara la lista de tareas

class TaskCreateView(LoginRequiredMixin, CreateView): # Esta es la vista que agregara tareas
    login_required = True
    model = Task # Aqui especificamos la tabla
    template_name = "todo_task_form.html" # Aqui especificamos el html que motrara el formulario
    fields = ['title', 'completed'] # Aqui especificamos los campos de la tabla que se mostraran en el formulario
    success_url = "/tasks/" # Aqui especificamos la ruta donde se redireccionara 
    # una vez que se crea una tarea

class TaskUpdateView(LoginRequiredMixin, UpdateView): # Esta es la vista que edita las tareas
    login_required = True
    model = Task # Aqui especificamos la tabla
    template_name = "todo_task_form.html" # Aqui especificamos el html que mostrara el formulario
    fields = ['title', 'completed'] # Aqui especificamos los campos de la tabla que se mostraran en el formulario
    success_url = "/tasks/" # Aqui especificamos la ruta donde se redireccionara 
    # una vez que se edita una tarea

class TaskDeleteView(LoginRequiredMixin, DeleteView): # Esta es la vista que aliminara las tareas
    login_required = True
    model = Task # Aqui especificamos la tabla
    template_name = "todo_task_confirm_delete.html" # Aqui especificamos el html que confirmara la eliminacion
    success_url = "/tasks/" # Aqui especificamos la ruta donde se redireccionara 
    # una vez que se elimina una tarea
