
from django.shortcuts import render
from rest_framework import  viewsets,mixins
from Journey.serializers import JourneySerializer
from Journey.models import trip
from accounts.permissions import HasValidAPIKey
# Create your views here.
class JourneyViewSet(viewsets.ModelViewSet):
    
    queryset = trip.objects.all()
    serializer_class = JourneySerializer
    permission_classes = []
    def list(self, request):
        return super().list(request)

    def create(self, request):
         return super().create(request)

    def retrieve(self, request, pk=None):
        return super().retrieve(request,pk)

    def update(self, request, pk=None):
        return super().retrieve(request,pk)

    def partial_update(self, request, pk=None):
        return super().retrieve(request,pk)

    def destroy(self, request, pk=None):
        return super().retrieve(request,pk)