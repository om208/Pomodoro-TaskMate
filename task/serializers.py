from rest_framework import serializers
from .models import User, Task, PomodoroSession, Settings, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'google_oauth_token', 'github_oauth_token']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        if data['task_deadline'] <= data['entry_date']:
            raise serializers.ValidationError("Task deadline must be greater than created_on.")
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