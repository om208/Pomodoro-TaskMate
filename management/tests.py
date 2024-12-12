from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Task
from django.contrib.auth.models import User
from .models.pomodoro_session import PomodoroSession
from .models.user_settings import ManagementSettings

# User Table Endpoints Test

class UserAuthTests(APITestCase):
    def test_user_signup(self):
        url = reverse('signup')
        data = {
            'email': 'test@example.com',
            'password': 'TestPass123!',
            'confirm_password': 'TestPass123!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_signup_duplicate_email(self):
        User.objects.create_user(email='test@example.com', password='TestPass123!')
        url = reverse('signup')
        data = {
            'email': 'test@example.com',
            'password': 'TestPass123!',
            'confirm_password': 'TestPass123!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login(self):
        User.objects.create_user(email='test@example.com', password='TestPass123!')
        url = reverse('login')
        data = {
            'email': 'test@example.com',
            'password': 'TestPass123!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login_invalid_credentials(self):
        url = reverse('login')
        data = {
            'email': 'nonexistent@example.com',
            'password': 'WrongPass!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

# Task Table Endpoints Test

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_task(self):
        data = {
            "userId": str(self.user.id),
            "title": "Test Task",
            "description": "Test Description",
            "deadline": "2023-12-31T23:59:59Z",
            "priority": "medium",
            "estimated_time": 60,
            "remainder_sound": "/reminder-sound/Task/bell1",
            "Reminder_duration": 30
        }
        response = self.client.post('/api/tasks/add/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data['success'])

    def test_get_tasks(self):
        response = self.client.get(f'/api/tasks/?userId={self.user.id}')
        self.assertEqual(response.status_code, 200)

class PomodoroSessionTests(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(
            user_id=1,  # Replace with a valid user ID
            title="Test Task",
            description="Test Description",
            initial_deadline="2023-10-15T10:00:00Z",
            deadline="2023-10-20T17:00:00Z",
            priority="HIGH",
            estimated_time=5,
            remainder_sound="/reminder-sound/Task/bell1",
            status="PENDING",
            Reminder_duration=30
        )

    def test_start_pomodoro_session(self):
        url = reverse('start-pomodoro-session')
        data = {"task_id": self.task.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('session_id', response.data)
        self.assertIn('start_time', response.data)

    def test_stop_pomodoro_session(self):
        session = PomodoroSession.objects.create(task=self.task)
        url = reverse('stop-pomodoro-session', args=[session.id])
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('success', response.data)
        self.assertIn('duration', response.data)

class ManagementSettingsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        self.settings = ManagementSettings.objects.create(user=self.user, goal='Data Science', alarm_tune='Tune1', progress_status='NOT_STARTED')

    def test_get_settings(self):
        response = self.client.get(f'/api/settings/?userId={self.user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['goal'], 'Data Science')

    def test_update_settings(self):
        response = self.client.put('/api/settings/update/', {'userId': self.user.id, 'goal': 'Machine Learning', 'alarm_tune': 'Tune2'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['success'])

    def test_get_progress_status(self):
        response = self.client.get(f'/api/settings/progress_status/?userId={self.user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['progress_status'], 'NOT_STARTED')
