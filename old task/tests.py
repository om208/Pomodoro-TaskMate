from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task, PomodoroSession, Settings, Notification

class TaskManagementTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            initial_task_deadline='2023-12-01T00:00:00Z',
            task_deadline='2023-12-01T00:00:00Z',
            estimate_time='01:00:00',
            priority='medium',
            remainder_time_interval='00:30:00',
            remainder_sound='double beep sound',
            delay_days=0,
            status='pending',
            user=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.user.username, 'testuser')

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        url = reverse('task-list')
        data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'initial_task_deadline': '2023-12-01T00:00:00Z',
            'task_deadline': '2023-12-01T00:00:00Z',
            'estimate_time': '01:00:00',
            'priority': 'medium',
            'remainder_time_interval': '00:30:00',
            'remainder_sound': 'double beep sound',
            'delay_days': 0,
            'status': 'pending',
            'user': self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

class PomodoroSessionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            initial_task_deadline='2023-12-01T00:00:00Z',
            task_deadline='2023-12-01T00:00:00Z',
            estimate_time='01:00:00',
            priority='medium',
            remainder_time_interval='00:30:00',
            remainder_sound='double beep sound',
            delay_days=0,
            status='pending',
            user=self.user
        )

    def test_create_pomodoro_session(self):
        url = reverse('pomodoro-list')
        data = {
            'task': self.task.id,
            'start_time': '2023-12-01T00:00:00Z',
            'end_time': '2023-12-01T00:25:00Z',
            'status': 'working'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PomodoroSession.objects.count(), 1)
        self.assertEqual(PomodoroSession.objects.get().task.title, 'Test Task')

class SettingsTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.settings = Settings.objects.create(
            user=self.user,
            alarm_tune='Bell1',
            ultimate_goal='backend data engineer',
            progress_status='average',
            suggestion='complete tasks on time'
        )

    def test_get_settings(self):
        url = reverse('settings-detail', args=[self.settings.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['alarm_tune'], 'Bell1')

class NotificationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.notification = Notification.objects.create(
            user=self.user,
            message='Task deadline is near',
            read_status=False
        )

    def test_get_notifications(self):
        url = reverse('notification-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['message'], 'Task deadline is near')
