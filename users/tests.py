from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import CustomUser


class CreateUserTestCase(APITestCase):

    def test_registration(self):
        """checks if a customer can register on the system"""
        data = {'username': 'maistodos',
                'email':'mais@todos.com',
                'password1': 'pythonDRF',
                'password2': 'pythonDRF'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)