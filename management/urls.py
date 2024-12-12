# management/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdditionalTestingView, SignUpView, LoginView, OAuthView
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView
from .views import StartPomodoroSessionView, StopPomodoroSessionView
from .views import GetSettings, UpdateSettings, GetProgressStatus, CreateSettingsView

urlpatterns = [
    path('', AdditionalTestingView, name='AdditionalTestingView'),
    path('auth/signup/', SignUpView.as_view(), name='signup'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/oauth/', OAuthView.as_view(), name='oauth'),
    # Task table endpoint
    path('tasks/', TaskListView.as_view(), name='task-list'),   # tasks/?userId=<USER_ID>
    path('tasks/add/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/edit/', TaskUpdateView.as_view(), name='task-update'),   # tasks/edit/?userId=<task_id>/
    path('tasks/delete/', TaskDeleteView.as_view(), name='task-delete'),  # tasks/delete/?userId=<task_id>/
    # Add more URL patterns here
    path('pomodoro/start/', StartPomodoroSessionView.as_view(), name='start-pomodoro-session'),
    path('pomodoro/stop/', StopPomodoroSessionView.as_view(), name='stop-pomodoro-session'),   
    # Settings Table Endpoints
    path('settings/', GetSettings.as_view(), name='get_settings'),  # settings/?userId=<userId>
    path('settings/update/', UpdateSettings.as_view(), name='update_settings'),
    path('settings/progress_status/', GetProgressStatus.as_view(), name='get_progress_status'),   # settings/progress_status/?userId=<userId>
    path('settings/add/', CreateSettingsView.as_view(), name='create_settings'),
   
]