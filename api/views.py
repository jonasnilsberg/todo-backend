from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status, permissions


# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def TaskList(request):
    tasks = Task.objects.filter(user=request.user)
    serializers = TaskSerializer(tasks, many=True, context = {'request': request})
    return Response(serializers.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TaskDetail(request, pk):
    task = Task.objects.get(id=pk)
    if task.user != request.user:
        return Response({"Error": "No access"})
    serializer = TaskSerializer(task, many=False, context = {'request': request})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def TaskCreate(request):
    serializer = TaskSerializer(data=request.data, context = {'request': request})
    if serializer.is_valid():
        serializer.save(user=request.user)
    else:
        Response({"Error": "Data not valid"})
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def TaskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data, context = {'request': request})
    if serializer.is_valid():
        serializer.save(user=request.user)
    return Response(serializer.data)