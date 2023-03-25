from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path("", views.IndexView.as_view(), name="task_list"),
    path("create/", views.CreateTaskView.as_view(), name="create_task"),
    path("update/<int:pk>/", views.TaskUpdateView.as_view(), name="update_task"),
    path("complete/<int:pk>/", views.completeTask, name="complete_task"),
    path("delete/<int:pk>/", views.deleteTask, name="delete_task"),
]
