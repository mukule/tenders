from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ProcurementMethod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CitizenContractor(models.Model):
    tender_title = models.CharField(
        max_length=100, null=True, default='Untitled')
    tender_ref = models.CharField(max_length=100, unique=True)
    tender_files = models.FileField(upload_to='tenders/')
    addendums = models.FileField(upload_to='addendums/', blank=True)
    certifications = models.FileField(upload_to='certifications/', blank=True)
    drawings = models.FileField(upload_to='drawings/', blank=True)
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()
    procurement_method = models.ForeignKey(
        ProcurementMethod, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    awarded_status = models.BooleanField(default=False)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    awarded = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.tender_title


class OpenInternational(models.Model):
    tender_title = models.CharField(
        max_length=100, null=True, default='Untitled')
    tender_ref = models.CharField(max_length=100, unique=True)
    tender_files = models.FileField(upload_to='tenders/')
    addendums = models.FileField(upload_to='addendums/', blank=True)
    certifications = models.FileField(upload_to='certifications/', blank=True)
    drawings = models.FileField(upload_to='drawings/', blank=True)
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()
    procurement_method = models.ForeignKey(
        ProcurementMethod, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    awarded_status = models.BooleanField(default=False)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    awarded = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.tender_title


class OpenNational(models.Model):
    tender_title = models.CharField(
        max_length=100, null=True, default='Untitled')
    tender_ref = models.CharField(max_length=100, unique=True)
    tender_files = models.FileField(upload_to='tenders/')
    addendums = models.FileField(upload_to='addendums/', blank=True)
    certifications = models.FileField(upload_to='certifications/', blank=True)
    drawings = models.FileField(upload_to='drawings/', blank=True)
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()
    procurement_method = models.ForeignKey(
        ProcurementMethod, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    awarded_status = models.BooleanField(default=False)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    awarded = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.tender_title


class ReservedPWD(models.Model):
    tender_title = models.CharField(
        max_length=100, null=True, default='Untitled')
    tender_ref = models.CharField(max_length=100, unique=True)
    tender_files = models.FileField(upload_to='tenders/')
    addendums = models.FileField(upload_to='addendums/', blank=True)
    certifications = models.FileField(upload_to='certifications/', blank=True)
    drawings = models.FileField(upload_to='drawings/', blank=True)
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()
    procurement_method = models.ForeignKey(
        ProcurementMethod, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    awarded_status = models.BooleanField(default=False)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    awarded = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.tender_title


class ReservedWomen(models.Model):
    tender_title = models.CharField(
        max_length=100, null=True, default='Untitled')
    tender_ref = models.CharField(max_length=100, unique=True)
    tender_files = models.FileField(upload_to='tenders/')
    addendums = models.FileField(upload_to='addendums/', blank=True)
    certifications = models.FileField(upload_to='certifications/', blank=True)
    drawings = models.FileField(upload_to='drawings/', blank=True)
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()
    procurement_method = models.ForeignKey(
        ProcurementMethod, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    awarded_status = models.BooleanField(default=False)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    awarded = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.tender_title


class ReservedYouth(models.Model):
    tender_title = models.CharField(
        max_length=100, null=True, default='Untitled')
    tender_ref = models.CharField(max_length=100, unique=True)
    tender_files = models.FileField(upload_to='tenders/')
    addendums = models.FileField(upload_to='addendums/', blank=True)
    certifications = models.FileField(upload_to='certifications/', blank=True)
    drawings = models.FileField(upload_to='drawings/', blank=True)
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()
    procurement_method = models.ForeignKey(
        ProcurementMethod, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    awarded_status = models.BooleanField(default=False)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    awarded = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.tender_title


class Product_category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    TITLE_CHOICES = [
        ('Mr', 'Mr'),
        ('Ms', 'Ms'),
    ]

    company_name = models.CharField(max_length=100)
    duns_number = models.CharField(max_length=20, null=True, blank=True)
    language = models.CharField(max_length=50)
    tax_jurisdiction_code = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    vendor_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_category = models.ManyToManyField(Product_category)
    country = models.CharField(max_length=50)
    region_district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    company_postal_code = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    title = models.CharField(max_length=50, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.company_name
