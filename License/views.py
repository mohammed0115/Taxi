
from django.shortcuts import render
from rest_framework import  viewsets,mixins
from License.serializers import LicenseSerializer
from License.models import License
from accounts.permissions import HasValidAPIKey
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
# Create your views here.
class LicenseViewSet(viewsets.ModelViewSet):
    
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    permission_classes = []




class SearchForLicense(APIView):
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
  
        if self.isindict(data,'issueDate'):
            search['issueDate']=data['issueDate']
        if self.isindict(data,'expDate'):
            search['expDate']=data['expDate']
        if self.isindict(data,'License_type'):
            search['License_type']=data['License_type']
        if self.isindict(data,'id'):
            search['id']=data['id']
        if self.isindict(data,'issuePlace'):
            search['issuePlace']=data['issuePlace']
       
        else:
            context={"error":"wrong fields "}
        
        if len(search)==0:
            return Response(context)
        else:
            License_data = License.objects.filter(**search)
            # print(trip_data.values())
            context ={
            "message":"success",
            "search":License_data.values()
            }
            return Response(context,status=200)