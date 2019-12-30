from django.db import models
from Categories.models import Categories
# Create your models here.
class Vehicle(models.Model):
    chassNo = models.CharField(max_length=25)
    plateNo =models.IntegerField()
    color = models.CharField(max_length=20)
    model=models.CharField(max_length=90)
    year = models.IntegerField()
    Categories = models.ForeignKey(Categories, blank=True, null=True,on_delete=None)
    fuel=models.CharField(max_length=20)
    def __str__(self):
        return str("chassNo:",self.chassNo,"plateNo:",self.plateNo,"color:",self.color)
