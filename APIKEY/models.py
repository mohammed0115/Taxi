from django.db import models
from datetime import datetime
# Create your models here.
# from django.contrib.auth.models import AbstractUser
from accounts.models import user
import uuid
# from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class APIKey(models.Model):
    key = models.UUIDField(_('API key'), default=uuid.uuid4, editable=False)
    User = models.ForeignKey(user, on_delete=None)
    owner = models.CharField(max_length=100, null=False, blank=False)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.key)

    class Meta:
        verbose_name = 'API key'
        verbose_name_plural = 'API keys'


class BlockedToken(models.Model):
    token = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

