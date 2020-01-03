
from django.shortcuts import render
from rest_framework import  viewsets,mixins
from Vehicle.serializers import VehicleSerializer
from Vehicle.models import Vehicle
from accounts.permissions import HasValidAPIKey
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from Categories.models import Categories

class VehicleViewSet(viewsets.ModelViewSet):
    
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = []





class SearchForVehicle(APIView):
    authentication_classes = []
    permission_classes = []
    def isindict(self,Dict_data,key):
        if key in Dict_data:
            return True
        else:
            return False
    def post(self,request):
        data=request.data
        search={}
        context={}
        print (data)
        # color
        if self.isindict(data,'Categories'):
            c=data.pop('Categories')
            cat =Categories.objects.get(**c)
            search['Categories']=cat
        elif self.isindict(data,'chassNo'):
            search['chassNo']=data['chassNo']
        elif self.isindict(data,'plateNo'):
            search['plateNo']=data['plateNo']
        elif self.isindict(data,'color'):
            search['color']=data['color']
        elif self.isindict(data,'id'):
            search['id']=data['id']
        elif self.isindict(data,'year'):
            search['year']=data['year']
        elif self.isindict(data,'fuel'):
            search['fuel']=data['fuel']
        else:
            context={"error":"wrong fields "}
        
        if len(search)==0:
            return Response(context)
        else:
            Vehicle_data = Vehicle.objects.filter(**search)
            # print(trip_data.values())
            context ={
            "message":"success",
            "search":Vehicle_data.values()
            }
            return Response(context,status=200)