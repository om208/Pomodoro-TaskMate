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

# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'
#         read_only_fields = ('id', 'created_on', 'completed_on', 'initial_deadline')

# class TaskViewSet(viewsets.ViewSet):
#     def list(self, request):
#         user_id = request.query_params.get('userId')
#         if not user_id:
#             return Response(
#                 {"error": "userId is required"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        
#         tasks = Task.objects.filter(user_id=user_id)
#         serializer = TaskSerializer(tasks, many=True)
#         return Response({"tasks": serializer.data})

#     def create(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             task = serializer.save()
#             return Response({
#                 "success": True,
#                 "task_id": task.id
#             })
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk=None):
#         task = get_object_or_404(Task, pk=pk)
#         serializer = TaskSerializer(task, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success": True})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         task = get_object_or_404(Task, pk=pk)
#         task.delete()
#         return Response({"success": True})

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
