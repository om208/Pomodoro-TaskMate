from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    google_oauth_token = models.CharField(max_length=255, blank=True, null=True)
    github_oauth_token = models.CharField(max_length=255, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Add related_name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Add related_name to avoid conflict
        blank=True
    )

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    STATUS_CHOICES = [
        ('working', 'Working'),
        ('done', 'Done'),
        ('pending', 'Pending'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_task_deadline = models.DateTimeField()
    task_deadline = models.DateTimeField()
    estimate_time = models.DurationField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    remainder_time_interval = models.DurationField(default='00:30:00')
    remainder_sound = models.CharField(max_length=255, default='double beep sound')
    delay_days = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    start_time = models.DateTimeField(null=True, blank=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    task_complete_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PomodoroSession(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=Task.STATUS_CHOICES)

class Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alarm_tune = models.CharField(max_length=255, default='Bell1')
    ultimate_goal = models.CharField(max_length=255, default='backend data engineer', blank=True, null=True)
    progress_status = models.CharField(max_length=50, default='average')
    suggestion = models.CharField(max_length=255, default='complete tasks on time')

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    read_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
