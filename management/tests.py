from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Task
from django.contrib.auth.models import User

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
