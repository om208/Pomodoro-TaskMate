# management/urls.py
from django.urls import path
from .views import AdditionalTestingView, SignUpView, LoginView, OAuthView
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

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
]