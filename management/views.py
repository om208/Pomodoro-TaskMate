from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from .serializers import TaskSerializer, UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models.task import Task
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models.pomodoro_session import PomodoroSession
from datetime import datetime
from .models.user_settings import Settings
from django.contrib.auth.models import User
from .serializers import SettingsSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

def AdditionalTestingView(request):
    return HttpResponse("Welcome to the Management App Index Page.")

class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Account created."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "token": str(refresh.access_token),
                "user": {"id": str(user.id), "email": user.email}
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class OAuthView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        provider = request.data.get('provider')
        token = request.data.get('token')
        if provider not in ['Google', 'GitHub']:
            return Response({"error": "Invalid provider"}, status=status.HTTP_400_BAD_REQUEST)
        # OAuth implementation would go here
        # For now, return a placeholder response
        return Response({"message": "OAuth authentication not implemented yet."}, status=status.HTTP_501_NOT_IMPLEMENTED)

class TaskListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user_id = request.query_params.get('userId')
        tasks = Task.objects.filter(user_id=user_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response({'tasks': serializer.data})

class TaskCreateView(APIView):
    permission_classes = [AllowAny]
    # serializer_class = UserSerializer
    
    def post(self, request):
        data = request.data
        data['initial_deadline'] = data['deadline']
        print("Data", data)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True, 
                'task_id': serializer.data['id'],
                'task': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskUpdateView(APIView):
    permission_classes = [AllowAny]
    
    def put(self, request):
        task_id = request.query_params.get('task_id')
        task = get_object_or_404(Task, pk=task_id)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDeleteView(APIView):
    permission_classes = [AllowAny]
    
    def delete(self, request,):
        
        task_id = request.query_params.get('task_id')
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return Response({'success': True})

class StartPomodoroSessionView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        task_id = request.data.get('task_id')
        task = get_object_or_404(Task, pk=task_id)
        session = PomodoroSession.objects.create(task=task)
        return Response({
            "session_id": session.id,
            "start_time": session.start_time
        }, status=status.HTTP_201_CREATED)

class StopPomodoroSessionView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        session_id = request.data.get('session_id')
        session = get_object_or_404(PomodoroSession, pk=session_id)
        session.end_time = datetime.now()
        end_time = session.end_time
        start_time = PomodoroSession.objects.values_list('start_time', flat=True).get(pk=session_id)
        
        start_time_epoch = int(start_time.timestamp())
        end_time_epoch = int(end_time.timestamp())
        difference_in_minutes = (end_time_epoch - start_time_epoch) / 60
        session.save()
        return Response({
            "success": True,
            "duration": difference_in_minutes
        }, status=status.HTTP_200_OK)

class GetSettings(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user_id = request.query_params.get('userId')
        settings = Settings.objects.filter(user__id=user_id).first()
        if settings:
            return Response({
                "goal": settings.goal,
                "alarm_tune": settings.alarm_tune,
                "progress_status": settings.progress_status
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Settings not found"}, status=status.HTTP_404_NOT_FOUND)

class UpdateSettings(generics.GenericAPIView):
    serializer_class = SettingsSerializer
    permission_classes = [AllowAny]

    def put(self, request):
        user_id = request.data.get('user')
        goal = request.data.get('goal')
        alarm_tune = request.data.get('alarm_tune')
        progress_status = request.data.get('progress_status')

        settings = Settings.objects.filter(user__id=user_id).first()
        if settings:
            settings.goal = goal
            settings.alarm_tune = alarm_tune
            settings.progress_status = progress_status
            settings.save()
            return Response({"success": True}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Settings not found"}, status=status.HTTP_404_NOT_FOUND)

class GetProgressStatus(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user_id = request.query_params.get('userId')
        settings = Settings.objects.filter(user__id=user_id).first()
        if settings:
            return Response({
                "progress_status": settings.progress_status
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Settings not found"}, status=status.HTTP_404_NOT_FOUND)

class CreateSettingsView(generics.CreateAPIView):
    serializer_class = SettingsSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        user_id = request.data.get('user')
        goal = request.data.get('goal', 'Data Engineering')
        alarm_tune = request.data.get('alarm_tune')
        progress_status = request.data.get('progress_status')

        try:
            user = User.objects.get(id=user_id)
            settings = Settings.objects.create(
                user=user,
                goal=goal,
                alarm_tune=alarm_tune,
                progress_status=progress_status
            )
            return Response({
                "success": True,
                "settings": {
                    "user": settings.user.id,
                    "goal": settings.goal,
                    "alarm_tune": settings.alarm_tune,
                    "progress_status": settings.progress_status
                }
            }, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
