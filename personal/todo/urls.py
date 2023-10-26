from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

# Definir el nombre de la aplicacion
app_name = 'todo'

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name="task_list"),
    path('tasks/create/', TaskCreateView.as_view(), name="task_create"),
    path('tasks/edit/<int:pk>/', TaskUpdateView.as_view(), name="task_edit"),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name="task_delete"),
]