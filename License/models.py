from django.db import models

# Create your models here.
class License(models.Model):
    issueDate = models.DateField(blank=True, null=True)
    expDate = models.DateField(blank=True, null=True)
    License_type = models.CharField(max_length=50)
    issuePlace = models.CharField(max_length=90)