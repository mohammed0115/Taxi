
from django.shortcuts import render
from rest_framework import  viewsets,mixins
from Vehicle.serializers import VehicleSerializer
from Vehicle.models import Vehicle
from accounts.permissions import HasValidAPIKey

class VehicleViewSet(viewsets.ModelViewSet):
    
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = []