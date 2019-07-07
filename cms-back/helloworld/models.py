from django.db import models
from django.core.files.storage import default_storage



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
    intake_date = models.DateField()
    intake_source = models.CharField(max_length=30) 
    finished_quarantine_date = models.DateField()
    cat_id = models.IntegerField()
    cat_name = models.CharField(max_length=30)
    cat_photo = models.ImageField(upload_to='photos',null=True)
    cat_medical_history = models.FileField(upload_to='pdfs',null=True)
    mh_attached = models.BooleanField()
    fvrcp_vaccination = models.BooleanField()
    rabies_vaccination = models.BooleanField()
    
    

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

'''
type ( Intake Coordinator / Shelter Staff / Adoption Counsellors / Adoption Administrations / Pet Point Processing / Post-Adoption Team / Behaviour Counsellors / Animal Shelter Coordinator / Foster Coordinator / TCR Coordinator)
name
email
phone number?
'''

class Coordinator(models.Model):
    name = models.CharField(max_length=30)
    phone_number= models.CharField(max_length=80)


'''
intake source name (e.g. Toronto Animal Services North/West/East, return cat, move cat, or other)
contact(s) at this location
'''


class IntakeSource(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=80)
