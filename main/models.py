from django.db import models

class CitizenContractor(models.Model):
    tender_title = models.CharField(max_length=100, null=True, default='Untitled')
    tender_ref = models.CharField(max_length=100, unique=True)
    tender_files = models.FileField(upload_to='tenders/')
    addendums = models.FileField(upload_to='addendums/', blank=True)
    certifications = models.FileField(upload_to='certifications/', blank=True)
    drawings = models.FileField(upload_to='drawings/', blank=True)
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()

    def __str__(self):
        return self.tender_title
    
class OpenInternational(models.Model):
    tender_title = models.CharField(max_length=100, null=True, default='Untitled')
    tender_ref = models.CharField(max_length=100, unique=True)
    tender_files = models.FileField(upload_to='tenders/')
    addendums = models.FileField(upload_to='addendums/', blank=True)
    certifications = models.FileField(upload_to='certifications/', blank=True)
    drawings = models.FileField(upload_to='drawings/', blank=True)
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()

    def __str__(self):
        return self.tender_title


class OpenNational(models.Model):
    tender_title = models.CharField(max_length=100, null=True, default='Untitled')
    tender_ref = models.CharField(max_length=100, unique=True)
    tender_files = models.FileField(upload_to='tenders/')
    addendums = models.FileField(upload_to='addendums/', blank=True)
    certifications = models.FileField(upload_to='certifications/', blank=True)
    drawings = models.FileField(upload_to='drawings/', blank=True)
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()

    def __str__(self):
        return self.tender_title


class ReservedPWD(models.Model):
    tender_title = models.CharField(max_length=100, null=True, default='Untitled')
    tender_ref = models.CharField(max_length=100, unique=True)
    tender_files = models.FileField(upload_to='tenders/')
    addendums = models.FileField(upload_to='addendums/', blank=True)
    certifications = models.FileField(upload_to='certifications/', blank=True)
    drawings = models.FileField(upload_to='drawings/', blank=True)
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()

    def __str__(self):
        return self.tender_title


class ReservedWomen(models.Model):
    tender_title = models.CharField(max_length=100, null=True, default='Untitled')
    tender_ref = models.CharField(max_length=100, unique=True)
    tender_files = models.FileField(upload_to='tenders/')
    addendums = models.FileField(upload_to='addendums/', blank=True)
    certifications = models.FileField(upload_to='certifications/', blank=True)
    drawings = models.FileField(upload_to='drawings/', blank=True)
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()

    def __str__(self):
        return self.tender_title


class ReservedYouth(models.Model):
    tender_title = models.CharField(max_length=100, null=True, default='Untitled')
    tender_ref = models.CharField(max_length=100, unique=True)
    tender_files = models.FileField(upload_to='tenders/')
    addendums = models.FileField(upload_to='addendums/', blank=True)
    certifications = models.FileField(upload_to='certifications/', blank=True)
    drawings = models.FileField(upload_to='drawings/', blank=True)
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()

    def __str__(self):
        return self.tender_title
