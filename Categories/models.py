from django.db import models

# Create your models here.
class Categories (models.Model):
    name = models.CharField(max_length=90)
    price = models.FloatField(null=True)
    
    def __str__(self):
        return self.name
    # class Meta:
    #     abstract = True