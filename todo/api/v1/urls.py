from django.urls import path
from . import views

urlpatterns = [
    path("",views.TaskList.as_view(), name = "tasks_view"),
    path("<int:pk>",views.TaskDetail.as_view(), name = "task_detail"),
]
