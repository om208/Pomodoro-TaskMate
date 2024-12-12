from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

class Settings(models.Model):
    PROGRESS_STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal = models.CharField(max_length=255, default="Data Engineering")
    alarm_tune = models.CharField(max_length=255)
    progress_status = models.CharField(max_length=20, choices=PROGRESS_STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.goal}"