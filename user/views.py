from django.shortcuts import render
from .serializer import UserSerializer
from .models import User

from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status, permissions

from django.http import JsonResponse

from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

@api_view(["POST"])
def UserCreate(request):
    serializer = UserSerializer(data=request.data, many=False, context = {"request": request})
    if serializer.is_valid():
        print("valid")
        user = serializer.save()
    else:
        return Response(serializer.errors)
    return Response(get_tokens_for_user(user))


@api_view(["GET"])
def UserDetail(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False, context = {"request": request})
    return Response(serializer.data)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }