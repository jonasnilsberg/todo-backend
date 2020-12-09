from rest_framework import serializers
from .models import Task
from rest_framework.fields import CurrentUserDefault


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        exclude = ["user"]

