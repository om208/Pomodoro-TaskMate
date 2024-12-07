from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TaskViewSet, PomodoroSessionViewSet, SettingsViewSet, NotificationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'pomodoro', PomodoroSessionViewSet)
router.register(r'settings', SettingsViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]