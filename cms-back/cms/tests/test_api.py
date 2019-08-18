from datetime import date

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from rest_framework.test import APITestCase

from ..models import IntakeSource, Cat, FosterHome
from ..serializers import IntakeSourceSerializer, CatSerializer, FosterHomeSerializer


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

foster_home_data = {
    "name": "John Doe",
    "address": "123 Wallaby Lane",
    "contact_info": "test@test.com",
    "status": "Active",
    "home_environment": "Large Home",
    "car_ownership": True,
    "freestyle_notes": "Test Test Test",
}

coordinator_data = {
    "name": "test test test",
    "type": "test test test",
    "phone_number": "test test test",
    "email": "test test test",
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


class CoordinatorAPIViewTestCase(APITestCase):
    url = reverse("Coordinator")

    def test_valid_data(self):
        response = self.client.post(self.url, coordinator_data)
        self.assertEqual(201, response.status_code)


class FosterHomeAPIViewTestCase(APITestCase):
    url = reverse("FosterHome")

    def test_valid_data(self):
        response = self.client.post(self.url, foster_home_data)
        self.assertEqual(201, response.status_code)


class FosterHomeDetailAPIViewTestCase(APITestCase):
    def setUp(self):
        foster_home1 = foster_home2 = foster_home3 = foster_home4 = foster_home_data
        foster_home1["contact_info"] = "test1"
        foster_home2["contact_info"] = "test2"
        foster_home3["contact_info"] = "test3"
        foster_home4["contact_info"] = "test4"
        self.test1 = FosterHome.objects.create(**foster_home1)
        self.test2 = FosterHome.objects.create(**foster_home2)
        self.test3 = FosterHome.objects.create(**foster_home3)
        self.test4 = FosterHome.objects.create(**foster_home4)

    def test_get_id(self):
        response = self.client.get(reverse("fosterhomeID", kwargs={'pk': self.test1.pk}))
        self.assertEqual(response.data, FosterHomeSerializer(self.test1).data)


class CatDetailAPIViewTestCase(APITestCase):
    def setUp(self):
        cat1 = cat2 = cat3 = cat4 = cat_data
        cat1["cat_name"] = "test1"
        cat2["cat_name"] = "test2"
        cat3["cat_name"] = "test3"
        cat4["cat_name"] = "test4"
        self.test1 = Cat.objects.create(**cat1)
        self.test2 = Cat.objects.create(**cat2)
        self.test3 = Cat.objects.create(**cat3)
        self.test4 = Cat.objects.create(**cat4)

    def test_get_id(self):
        response = self.client.get(reverse("CatID", kwargs={'pk': self.test1.pk}))
        self.assertEqual(response.data, self.test1.data)


class IntakeSourceDetailAPIViewTestCase(APITestCase):
    def setUp(self):
        self.test1 = IntakeSource.objects.create(name="tester1", contact="tester1@test.com")
        self.test2 = IntakeSource.objects.create(name="tester2", contact="tester2@test.com")
        self.test3 = IntakeSource.objects.create(name="tester3", contact="tester3@test.com")
        self.test4 = IntakeSource.objects.create(name="tester4", contact="tester4@test.com")

    def test_get_id(self):
        response = self.client.get(reverse("IntakeID", kwargs={'pk': self.test1.pk}))
        self.assertEqual(response.data, IntakeSourceSerializer(self.test1).data)
