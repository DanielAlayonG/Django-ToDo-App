from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serializers import TaskSerializer
from tasks.models import Task
# Create your views here.

class task_view(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
