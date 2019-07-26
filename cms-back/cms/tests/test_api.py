from datetime import datetime, date

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from rest_framework.test import APITestCase

from ..models import Coordinator, IntakeSource, Cat, FosterHome
from ..serializers import CoordinatorSerializer, IntakeSourceSerializer, CatSerializer, FosterHomeSerializer


cat_data = {
    "status": "ADO",
    "propose_date": date.today(),
    "intake_date": date.today(),
    "intake_source": "Terry's House",
    "finished_quarantine_date": date.today(),
    "cat_id": 100,
    "cat_name": "Christopher",
    "cat_photo": SimpleUploadedFile(name='test.jpg', content=open("cms/tests/static/test.jpg", 'rb').read(), content_type='image/jpeg'),
    "cat_medical_history": SimpleUploadedFile('medical_history.txt', content=open("cms/tests/static/test.pdf", 'rb').read(), content_type='application/pdf'),
    "notes": "Test",
    "mh_attached": True,
    "spayed_neutered": True,
    "fvrcp_vaccination": True,
    "rabies_vaccination": True,
}


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


class CatAPIViewTestCase(APITestCase):
    url = reverse("Cat")

    def test_valid_data(self):
        response = self.client.post(self.url, cat_data)
        self.assertEqual(201, response.status_code)


class IntakeSourceDetailAPIViewTestCase(APITestCase):
    def setUp(self):
        self.test1 = IntakeSource.objects.create(name="tester1", contact="tester1@test.com")
        self.test2 = IntakeSource.objects.create(name="tester2", contact="tester2@test.com")
        self.test3 = IntakeSource.objects.create(name="tester3", contact="tester3@test.com")
        self.test4 = IntakeSource.objects.create(name="tester4", contact="tester4@test.com")

    def test_get_id(self):
        response = self.client.get(reverse("IntakeID", kwargs={'pk': self.test1.pk}))
        self.assertEqual(response.data, IntakeSourceSerializer(self.test1).data)
