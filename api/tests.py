import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

# Create your tests here.


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {"username": "TestUser", "email": "test@gmail.com", "password": "testpassword1",
                "first_name": "Test", "last_name": "Lopez"}
        response = self.client.post("/api/users/", data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

