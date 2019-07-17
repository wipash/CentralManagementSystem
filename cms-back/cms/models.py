from django.db import models
from django.core.files.storage import default_storage

class Cat(models.Model):
    CAT_STATUS = (
        ('PRO', 'Proposed'),
        ('INT', 'Intake'),
        ('FOS', 'Fostered'),
        ('ADO', 'Adopted'),
    )
    status = models.CharField(max_length=3, choices=CAT_STATUS)
    propose_date = models.DateField()
    intake_date = models.DateField()
    intake_source = models.CharField(max_length=30)
    finished_quarantine_date = models.DateField()
    cat_id = models.IntegerField()
    cat_name = models.CharField(max_length=30)
    cat_photo = models.ImageField(upload_to='photos',null=True)
    cat_medical_history = models.FileField(upload_to='pdfs',null=True)
    notes = models.CharField(max_length=100)
    mh_attached = models.BooleanField()
    spayed_neutered = models.BooleanField()
    fvrcp_vaccination = models.BooleanField()
    rabies_vaccination = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FosterHome(models.Model):
    STATUS = (
        ('ACT', 'Active'),
        ('INA', 'Inactive'),
        ('NAF', 'Not Allowed to Foster'),
    )
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    contact_info = models.CharField(max_length=80)
    status = models.CharField(max_length=10)
    home_environment = models.CharField(max_length=50)
    car_ownership = models.BooleanField()
    freestyle_notes = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Coordinator(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=40)
    phone_number= models.CharField(max_length=80)
    email = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class IntakeSource(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
