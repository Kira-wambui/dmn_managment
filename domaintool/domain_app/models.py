from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Domain(models.Model):
    name = models.CharField(max_length=200)
    registration_date = models.DateTimeField(verbose_name="Date registered", null=True, blank=True)
    expiry_date = models.DateTimeField(verbose_name="Date of expiry", null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class DomainInfo(models.Model):
    apiresponse = models.TextField()
    timestamp = models.DateTimeField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    
class Report(models.Model):
    title = models.CharField(max_length=200)
    report_date = models.DateField()
    report_generation_date = models.DateTimeField()
    generated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField()
    
    def __str__(self):
        return self.title