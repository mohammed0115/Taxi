from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .permissions import HasValidAPIKey
from accounts.serializers import UserSerializer
from accounts.models import user
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from datetime import datetime
from rest_framework.response import Response
from APIKEY.models import APIKey
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from accounts.permissions import HasValidAPIKey

from django.shortcuts import render
from rest_framework import  viewsets,mixins
from accounts.serializers import DriverSerializer,clientSerializer
from accounts.models import client,driver
from accounts.permissions import HasValidAPIKey

class UserViews(APIView):
    permission_classes = []
    def get(self,request,pk):
        queryset = user.objects.filter(pk=pk)
        return Response(queryset.values())
class UsersViews(APIView):
    permission_classes = []
    queryset   = user.objects.all()
    
    def get(self,request):
        return Response(self.queryset.values())
    



class driverViewSet(viewsets.ModelViewSet):
    
    queryset = driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = []
        

class ClientViewSet(viewsets.ModelViewSet):
    
    queryset = client.objects.all()
    serializer_class = clientSerializer
    permission_classes = []


class Register(APIView):
    permission_classes = []

    def post(self,request):
        data=JSONParser().parse(request)
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password, blank or null not allowed'},
                            status=HTTP_400_BAD_REQUEST)
        Serializer = UserSerializer(data=data,many=False)
        if Serializer.is_valid():
            Serializer.save()
            usr=user.objects.get(Serializer)
            key=APIKey()
            key.user=usr
            key.owner=usr
            key.save()
            data ={
                "error":False,
                "response message":"successfully registered",
                'token': key.key
            }
            return Response(data, status=201)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        












class Login(APIView):
    permission_classes=[]
    
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token= APIKey.objects.get(user=user)
        # print(token)
        return Response({'token': token.key,"ResponseMessage":"successful"},
                        status=HTTP_200_OK)

