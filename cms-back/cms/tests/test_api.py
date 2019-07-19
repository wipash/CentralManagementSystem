from django.urls import reverse

from rest_framework.test import APITestCase


class IntakeSourceAPIViewTestCase(APITestCase):
    url = reverse("IntakeSource")

    def test_invalid_data(self):
        user_data = {
            "name": "tester",
            "failed": 100,
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(400, response.status_code)

    def test_valid_data(self):
        user_data = {
            "name": "tester",
            "contact": "test@test.com",
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(201, response.status_code)
