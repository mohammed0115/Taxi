
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
    def isindict(self,Dict_data,key):
        if key in Dict_data:
            return True
        else:
            return False
    def post(self,request):
        data=request.data
        print (data)
        search={}
        context={}
        # 'startLat','startLon','endLat','endLon', 'price','distance','starttime','EndTime','Journey_type','stat',
        if self.isindict(data,'Categories'):
            c=data.pop('Categories')
            print(c)
            cat =Categories.objects.get(**c)
            search['Categories']=cat.id
        if self.isindict(data,'client'):
            cln=data.pop('client')
            clt =client.objects.get(**cln) 
            search['client']=clt.id
        if self.isindict(data,'driver'):
            cln=data.pop('driver')
            clt =client.objects.get(**cln) 
            search['driver']=clt.id
        if self.isindict(data,'startLat'):
            search['startLat']=data['startLat']
        if self.isindict(data,'startLon'):
            search['startLon']=data['startLon']
        if self.isindict(data,'id'):
            search['id']=data['id']
        if self.isindict(data,'endLat'):
            search['endLat']=data['endLat']
        if self.isindict(data,'endLon'):
            search['endLon']=data['endLon']
        if self.isindict(data,'price'):
            search['price']=data['price']
        if self.isindict(data,'distance'):
            search['distance']=data['distance']
        if self.isindict(data,'starttime'):
            search['starttime']=data['starttime']
        if self.isindict(data,'EndTime'):
            search['EndTime']=data['EndTime']
        if self.isindict(data,'Journey_type'):
            search['Journey_type']=data['Journey_type']
        if self.isindict(data,'stat'):
            search['stat']=data['stat']
        else:
            context={"error":"wrong fields "}
        if len(search)==0:
            return Response(context)
        else:
            trip_data = trip.objects.filter(**search)
            context ={
            "message":"success",
            "search":trip_data.values()
            }
            return Response(context,status=200)
        
       



        # c=data.pop('Categories')
        # cln=data.pop('client') 
        # drv=data.pop('driver')      
        # cat =Categories.objects.get(**c)
        # clt =client.objects.get(**cln)
        # drivr =driver.objects.get(**drv)
        # trip_data = trip.objects.filter(Categories=cat,client=clt,driver=drivr)
        # print(trip_data.values())
       
    
        # context ={
        #     "message":"success",
        #     "trip_search":trip_data.values()
        # }
        # return Response(context,status=200)