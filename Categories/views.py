from django.shortcuts import render
from rest_framework import  viewsets,mixins
from Categories.serializers import CategoriesSerializer
from Categories.models import Categories
from accounts.permissions import HasValidAPIKey
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class CategoriesViewSet(viewsets.ModelViewSet):
    
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = []

class SearchForCategories(APIView):
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
  
        if self.isindict(data,'name'):
            search['name']=data['name']
        if self.isindict(data,'price'):
            search['price']=data['price']
        if self.isindict(data,'id'):
            search['id']=data['id']
       
        else:
            context={"error":"wrong fields "}
        
        if len(search)==0:
            return Response(context)
        else:
            Categories_data = Categories.objects.filter(**search)
            # print(trip_data.values())
            context ={
            "message":"success",
            "trip_search":Categories_data.values()
            }
            return Response(context,status=200)