from django.test import TestCase
from ..models import IntakeSource


class IntakeSourceTest(TestCase):
    def setUp(self):
        IntakeSource.objects.create(name='Nataly', contact='nataly@test.com')
        IntakeSource.objects.create(name='Sean', contact='sean@test.com')

    def test_intake_contact(self):
        intake_nataly = IntakeSource.objects.get(name='Nataly')
        intake_sean = IntakeSource.objects.get(name='Sean')
        self.assertEqual(
            intake_nataly.contact, "nataly@test.com")
        self.assertEqual(
            intake_sean.contact, "sean@test.com")
