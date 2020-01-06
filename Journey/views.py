import operator
from django.db.models import Q
from Journey.Query import Query 
from Journey.Query import get_query
from Journey.Query import get_query__endswith
from Journey.Query import get_query__startswith
from Journey.Query import get_query__lte
from Journey.Query import get_query__lt
from Journey.Query import get_query__gte
from Journey.Query import get_query__gt
from Journey.Query import get_query__

from functools import reduce
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
    def getMyQ(self,data):
        query_list=[]
        for i in data:
            l=[]
            l.append(i)
            if "__gte" in i.strip():
                
               x=get_query__(str(data[i]),l)
               query_list.append(x)
            elif "__lte" in i.strip():
                x=get_query__(str(data[i]),l)
                query_list.append(x)
            elif "__gt" in i.strip():
                x=get_query__(str(data[i]),l)
                query_list.append(x)
            elif "__lt" in i.strip():
                x=get_query__(str(data[i]),l)
                query_list.append(x)
            elif "__startswith" in i.strip():
                x=get_query__(str(data[i]),l)
                query_list.append(x)
            elif "__endswith" in i.strip():
                x=get_query__(str(data[i]),l)
                query_list.append(x)
                
            else:

                x=get_query(str(data[i]),l)
                print(x)
                query_list.append(x)
        return query_list

    def getSep(self,query_list,sep):
        query=Q()
        if sep['sep']==1 :
            for j in query_list:
                query&=j
        else:
            for j in query_list:
                query|=j
                
        return query 
    def post(self,request):
        data=request.data
        sep={"sep":4}
        if self.isindict(data,'sep'):
            sep['sep']=data.pop('sep')
            print("sep===>",sep)
        else:
            sep['sep']=4
        if sep.get('sep')==4:
            return Response({"message":"Error"},status=404)
        else:
            query=self.getSep(self.getMyQ(data),sep)
            t=trip.objects.filter(query)
            context={
                "Search":t.values(),
               
                 }
            return Response(context,status=200)        