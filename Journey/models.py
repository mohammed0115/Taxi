from django.db import models

# Create your models here.

from Categories.models import Categories
from accounts.models import driver,client
class trip (models.Model):
    TYPE_CHOICES= ((0,'OPEN'),(1,'CLOSE'))
    STATUS_CHOICE=((1,'REQUEST'),(2,'WAIT DRIVER RESPONSE'),
    (3,'DRIVER ACCEPT'),(4,'DRIVER ARRIVE'),(5,'STAR TRIP'),(6,'FINISH'),(7,'PAID'),(9,'REJECT'))
    startLat = models.FloatField()
    startLon = models.FloatField()
    endLat   = models.FloatField()
    endLon   = models.FloatField()
    price    = models.FloatField()
    distance = models.IntegerField()
    # starttime = models.TimeField(verbose_name=None, name=None,null=True, auto_now=False, auto_now_add=False)
    # EndTime   = models.TimeField(verbose_name=None, name=None,null=True, auto_now=False, auto_now_add=False)
    starttime = models.IntegerField()
    EndTime   = models.IntegerField()
    Journey_type = models.IntegerField(default=1, choices=TYPE_CHOICES)
    stat = models.IntegerField(default=1, choices=STATUS_CHOICE)
    Categories = models.ForeignKey(Categories, blank=True, null=True,on_delete=None)
    driver = models.ForeignKey(driver, blank=True, null=True,on_delete=None)
    client = models.ForeignKey(client, blank=True, null=True,on_delete=None)

    # code= models.BigIntegerField(max_length=30)
    # cust= models.IntegerField(max_length=20)
    # stat=models.IntegerField(max_length=2)
    # clatlng= models.CharField(max_length=100,null=true)
    # dlatlng= models.CharField(max_length=100,null=true)
    # dist=models.CharField(max_length=30,null=true)
    # sta=models.CharField(max_length=100,null=true)
    # end= models.CharField(max_length=100,null=true)
    # car=models.IntegerField(max_length=2)
    # price= models.CharField(max_length=20,null=true)
    # from_address=models.CharField(max_length=200,null=true)
    # to_address=models.CharField(max_length=200,null=true)
    # drv_pass=models.IntegerField(max_length=11)


