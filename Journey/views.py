
from django.shortcuts import render
from rest_framework import  viewsets,mixins
from Journey.serializers import JourneySerializer
from Journey.models import Journey
from accounts.permissions import HasValidAPIKey
# Create your views here.
class JourneyViewSet(viewsets.ModelViewSet):
    
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    permission_classes = [HasValidAPIKey]