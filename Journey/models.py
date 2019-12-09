from django.db import models

# Create your models here.

from Categories.models import Categories
from accounts.models import user
class Journey (models.Model):
    TYPE_CHOICES= ((0,'OPEN'),(1,'CLOSE'))
    STATUS_CHOICE=((1,'REQUEST'),(2,'DRIVER RESPONSE'),(3,'END'),(4,'CANCEL'),(5,'DECLINE'))
    startLat = models.FloatField()
    startLon = models.FloatField()
    endLat   = models.FloatField()
    endLon   = models.FloatField()
    price    = models.FloatField()
    distance = models.IntegerField()
    starttime = models.TimeField(verbose_name=None, name=None, auto_now=False, auto_now_add=False)
    EndTime   = models.TimeField(verbose_name=None, name=None, auto_now=False, auto_now_add=False)
    Journey_type = models.IntegerField(default=1, choices=TYPE_CHOICES)
    status = models.IntegerField(default=1, choices=STATUS_CHOICE)
    Categories = models.ForeignKey(Categories, blank=True, null=True,on_delete=None)
    user = models.ForeignKey(user, blank=True, null=True,on_delete=None)


