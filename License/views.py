
from django.shortcuts import render
from rest_framework import  viewsets,mixins
from License.serializers import LicenseSerializer
from License.models import License
from accounts.permissions import HasValidAPIKey

# Create your views here.
class LicenseViewSet(viewsets.ModelViewSet):
    
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    permission_classes = []