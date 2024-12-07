from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, Task, PomodoroSession, Settings, Notification
from .serializers import UserSerializer, TaskSerializer, PomodoroSessionSerializer, SettingsSerializer, NotificationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PomodoroSessionViewSet(viewsets.ModelViewSet):
    queryset = PomodoroSession.objects.all()
    serializer_class = PomodoroSessionSerializer
    permission_classes = [IsAuthenticated]

class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = [IsAuthenticated]

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
