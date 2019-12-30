from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import AbstractUser,BaseUserManager
# from User.models import *
import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from License.models import License
from Vehicle.models import Vehicle
# GENDER_CHOICES = ((0, 'Female'),(1, 'Male'), )
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)




class user(AbstractUser):
    USER_TYPE_ADMIN=0
    USER_TYPE_DRIVER=1
    USER_TYPE_CLIENT=3


    GENDER_CHOICES = ((0, 'Female'),(1, 'Male'), )
    
    USER_TYPE_CHOICES = (
        (USER_TYPE_ADMIN, 'Admin'),
        (USER_TYPE_DRIVER, 'DRIVER'),
        (USER_TYPE_CLIENT, 'CLIENT'),
    )
    username =models.CharField(max_length=90)
    # user_type = models.IntegerField(default=USER_TYPE_ADMIN, choices=USER_TYPE_CHOICES)
    phone =models.CharField(max_length=20, blank=True, null=True)
    address=models.CharField(max_length=90,null=True)
    email=models.EmailField(('email address'), unique=True, db_index=True, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender=models.IntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    # lat= models.FloatField(max_length=20,null=True)
    # lon =models.FloatField(max_length=20,null=True)
    # status=models.IntegerField(choices=STATUS_CHOICE, blank=True, null=True)
    # bloodClass=models.CharField(max_length=5,null=True)
    # License = models.ForeignKey(License, blank=True, null=True,on_delete=None)
    # # Vehicle = models.ForeignKey(Vehicle, blank=True, null=True,on_delete=None)
    objects = UserManager()
    user_permissions=User.user_permissions
    groups=User.groups
    # objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # remove email  
class client(AbstractUser):
    GENDER_CHOICES = ((0, 'Female'),(1, 'Male'), )
    username =models.CharField(max_length=90)
    phone =models.CharField(max_length=20, blank=True, null=True)
    address=models.CharField(max_length=90,null=True)
    email=models.EmailField(('email address'), unique=True, db_index=True, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender=models.IntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    objects = UserManager()
    user_permissions=User.user_permissions
    groups=User.groups
    class Meta:
        verbose_name_plural="Client"
class driver(AbstractUser):
    GENDER_CHOICES = ((0, 'Female'),(1, 'Male'), )
    STATUS_CHOICE=((0,'ACTIVE'),(1,'UNACTIVE'))
    username =models.CharField(max_length=90)
    phone =models.CharField(max_length=20, blank=True, null=True)
    Vehicle = models.ForeignKey(Vehicle, blank=True, null=True,on_delete=None)
    address=models.CharField(max_length=90,null=True)
    email=models.EmailField(('email address'), unique=True, db_index=True, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender=models.IntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    lat= models.FloatField(max_length=20,null=True)
    lon =models.FloatField(max_length=20,null=True)
    status=models.IntegerField(choices=STATUS_CHOICE, blank=True, null=True)
    bloodClass=models.CharField(max_length=5,null=True)
    License = models.ForeignKey(License, blank=True, null=True,on_delete=None)
    objects = UserManager()
    user_permissions=User.user_permissions
    groups=User.groups
    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural="Driver"
    
