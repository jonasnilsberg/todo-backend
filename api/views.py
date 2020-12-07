from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status, permissions


# Create your views here.

class TaskView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        print(request.user.email)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True, context = {'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def TaskList(request):
    tasks = Task.objects.all()
    serializers = TaskSerializer(tasks, many=True, context = {'request': request})
    return Response(serializers.data)


@api_view(['GET'])
def TaskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False, context = {'request': request})
    return Response(serializer.data)


@api_view(['POST'])
def TaskCreate(request):
    serializer = TaskSerializer(data=request.data, context = {'request': request})
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def TaskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data, context = {'request': request})
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)