from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('',views.TaskViewSet, 'task')

# urlpatterns = [
#     # path("",views.TaskList.as_view(), name = "tasks_view"),
#     # path("<int:pk>",views.TaskDetail.as_view(), name = "task_detail"),
#     path("",views.TaskViewSet.as_view({'get':'list','post':'create'}), name = "tasks_view"),
#     path("<int:pk>/",views.TaskViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}), name = "task_view"),
    
# ]
urlpatterns = router.urls
