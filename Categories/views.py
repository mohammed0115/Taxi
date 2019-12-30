from django.shortcuts import render
from rest_framework import  viewsets,mixins
from Categories.serializers import CategoriesSerializer
from Categories.models import Categories
from accounts.permissions import HasValidAPIKey
# Create your views here.
class CategoriesViewSet(viewsets.ModelViewSet):
    
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = []