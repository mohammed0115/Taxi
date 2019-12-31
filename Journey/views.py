
from django.shortcuts import render
from rest_framework import  viewsets,mixins
from Journey.serializers import JourneySerializer
from Journey.models import trip
from Categories.models import Categories
from accounts.permissions import HasValidAPIKey

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from accounts.models import client, driver
# Create your views here.
class JourneyViewSet(viewsets.ModelViewSet):
    
    queryset = trip.objects.all()
    serializer_class = JourneySerializer
    permission_classes = []
    
class SearchForTrip(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self,request):
        data=request.data
        print (data)
        c=data.pop('Categories')
        cln=data.pop('client') 
        drv=data.pop('driver')      
        cat =Categories.objects.get(**c)
        clt =client.objects.get(**cln)
        drivr =driver.objects.get(**drv)
        trip_data = trip.objects.filter(Categories=cat,client=clt,driver=drivr)
        print(trip_data.values())
       
    
        context ={
            "message":"success",
            "trip_search":trip_data.values()
        }
        return Response(context,status=200)