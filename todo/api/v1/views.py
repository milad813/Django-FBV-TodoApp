from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import TaskSerializer
from ...models import Task
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import viewsets



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    # def list(self, request):
    #     serializer = self.serializer_class(self.queryset, many=True)
    #     return Response(serializer.data)
    
    # def create(self, request):
    #     serializer = self.serializer_class(request.data)
    #     serializer.save()
    #     return Response(serializer.data)
    
    # def update(self, request, pk=None):
    #     task=self.queryset.get(pk=pk)
    #     serializer = self.serializer_class(task, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    
    # def retrieve(self, request, pk=None):
    #     task_detail = self.queryset.get(pk=pk)
    #     serializer = self.serializer_class(task_detail)
    #     return Response(serializer.data)
    
    # def destroy(self, request, pk=None):
    #     task = self.queryset.get(pk=pk)
    #     task.delete()
    #     return Response({'Item deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
    


class TaskList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

# class TaskList(APIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = TaskSerializer

#     def get(self, request):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         task = TaskSerializer(data=request.data)
#         task.is_valid(raise_exception=True)
#         task.save()
#         return Response(task.data)

class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    
    
# class TaskDetail(APIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = TaskSerializer
#     def get(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         sertializer = TaskSerializer(task)
#         return Response(sertializer.data)

#     def put(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         sertializer = TaskSerializer(task, data=request.data)
#         sertializer.is_valid(raise_exception=True)
#         sertializer.save()
#         return Response(sertializer.data)

#     def delete(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         task.delete()
#         return Response({"status": "object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
# def tasks_list(request):
#     if request.method == 'GET':
#         tasks= Task.objects.all()
#         serializer = TaskSerializer (tasks, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         task = TaskSerializer(data=request.data)
#         task.is_valid(raise_exception=True)
#         task.save()
#         return Response(task.data)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        sertializer = TaskSerializer(task)
        return Response(sertializer.data)
    elif request.method == 'PUT':
        sertializer = TaskSerializer(task, data=request.data)
        sertializer.is_valid(raise_exception=True)
        sertializer.save()
        return Response(sertializer.data)
    elif request.method == 'DELETE':
        task.delete()
        return Response({"status": "object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
