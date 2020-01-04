from django.contrib.auth.models import  Group
from rest_framework import serializers
# from Basic_salary.models import Temp_Employee

from rest_framework import serializers
from accounts.serializers import UserSerializer
from Journey.models import trip
from accounts.models import client
from accounts.models import driver
from Categories.models import Categories

class CategoriesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField()
    class Meta:
        model=Categories
        

class clientSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)
    class Meta:
        model=client
        
class DriverSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)
    class Meta:
        model=driver
        

class JourneySerializer(serializers.ModelSerializer):
    # Categories=CategoriesSerializer()
    client=clientSerializer()
    # driver= DriverSerializer()
    
    class Meta:
        model = trip
        fields =['id','startLat','startLon','endLat','endLon', 'price','distance',
        'Journey_type','stat','client']
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        # Categories_data = validated_data.pop('Categories')
        client_data = validated_data.pop('client')
        # driver_data = validated_data.pop('driver')


        t = trip.objects.create(**validated_data)
        # print(Categories_data.get('name'))
        # cat, created = Categories.objects.get_or_create(**Categories_data)
        cln,created  =client.objects.get_or_create(**client_data)
        # drv,created  = driver.objects.get_or_create(**driver_data)
        # t.Categories=cat
        t.client=cln
        # t.driver=drv
        t.save()
        
        return t

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        Categories_data = validated_data.pop('Categories')
        client_data = validated_data.pop('client')
        driver_data = validated_data.pop('driver')



        instance.startLat = validated_data.get('startLat', instance.startLat)
        instance.startLon = validated_data.get('startLon', instance.startLon)
        instance.endLat = validated_data.get('endLat', instance.endLat)
        instance.endLon = validated_data.get('endLon', instance.endLon)
        instance.price = validated_data.get('price', instance.price)
        instance.distance = validated_data.get('distance', instance.distance)
        instance.starttime = validated_data.get('starttime', instance.starttime)
        instance.EndTime = validated_data.get('EndTime', instance.EndTime)
        instance.Journey_type = validated_data.get('Journey_type', instance.Journey_type)
        instance.stat = validated_data.get('stat', instance.stat)
        
        cat, created = Categories.objects.get_or_create(**Categories_data)
        
        cln,created  =client.objects.get_or_create(**client_data)
        
        drv,created  = driver.objects.get_or_create(**driver_data)
        

        instance.Categories = cat
        # instance.Categories=CategoriesSerializer.update(instance,validated_data)
        instance.client = cln
        instance.driver = drv

        instance.save()
        return instance
