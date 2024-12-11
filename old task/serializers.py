from rest_framework import serializers
from .models import User, Task, PomodoroSession, Settings, Notification
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'google_oauth_token', 'github_oauth_token', 'password']

class TaskSerializer(serializers.ModelSerializer):
    entry_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'  # Or li  st all fields explicitly

    def validate(self, data):
        task_deadline = data.get('task_deadline')
        # Use current time as entry_date
        entry_date = data.get('entry_date', timezone.now())
        if task_deadline and task_deadline < entry_date:
            raise serializers.ValidationError("Task deadline cannot be before the entry date.")
        return data

class PomodoroSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomodoroSession
        fields = '__all__'

    def validate(self, data):
        if data['end_time'] <= data['start_time']:
            raise serializers.ValidationError("End time must be greater than start time.")
        return data

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'