import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.conf import settings
from django.utils import timezone

class Task(models.Model):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    WORKING = 'working'
    DONE = 'done'
    PENDING = 'pending'
    STATUS_CHOICES = [
        (WORKING, 'Working'),
        (DONE, 'Done'),
        (PENDING, 'Pending'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_deadline = models.DateTimeField()
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default=MEDIUM)
    estimated_time = models.IntegerField(validators=[MinValueValidator(0)])
    remainder_sound = models.CharField(max_length=255, default="/reminder-sound/Task/bell1")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=PENDING)
    Reminder_duration = models.IntegerField(default=30, validators=[MinValueValidator(1)])
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # New instance
            self.initial_deadline = self.deadline
        if self.status == 'done' and not self.completed_on:
            self.completed_on = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} - {self.user.username}"