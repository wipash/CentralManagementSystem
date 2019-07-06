from django.db import models


'''
status * (proposed/intake/fostered/adopted/)
proposal date *
intake source *
intake date
finished quarantine date (always 2 weeks after intake date)
cat ID (shelter ID)
name
photo (support all image files)
medical history pdf/image (multiple)
notes
MH attached? y/n
spayed/neutered/neither
fvrcp vaccination (y/n)
rabies vaccination (y/n)
'''
class Cat(models.Model):
    CAT_STATUS = (
        ('PRO', 'Proposed'),
        ('INT', 'Intake'),
        ('FOS', 'Fostered'),
        ('ADO', 'Adopted'),
    )
    status = models.CharField(max_length=3, choices=CAT_STATUS)    
    propose_date = models.DateField()
    #intake_source = 
     
    mh_attached = models.BooleanField()


'''
name
address
contact info
status (active/inactive/not allowed to foster)
home environment (kids? other pets?)
car ownership (y/n)
free-style notes
'''

class FosterHome(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=80)

class Coordinator(models.Model):
    name = models.CharField(max_length=30)
    phone_number= models.CharField(max_length=80)

class IntakeSource(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=80)
