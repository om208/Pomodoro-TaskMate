# management/models/pomodoro_session.py

from django.db import models
from django.conf import settings
import uuid

class PomodoroSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey('management.Task', on_delete=models.CASCADE, related_name='pomodoro_sessions')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Pomodoro Session for {self.task.title} started at {self.start_time}"