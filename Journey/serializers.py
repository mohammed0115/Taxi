from django.contrib.auth.models import  Group
from rest_framework import serializers
# from Basic_salary.models import Temp_Employee

from rest_framework import serializers
from accounts.serializers import UserSerializer
from Journey.models import trip
from accounts.serializers import clientSerializer
from accounts.serializers import DriverSerializer
from Categories.serializers import CategoriesSerializer






class JourneySerializer(serializers.ModelSerializer):
    # Categories=CategoriesSerializer()
    # client=clientSerializer()
    # driver= DriverSerializer()
    
    class Meta:
        model = trip
        fields =['startLat','startLon','endLat','endLon', 'price','distance',
        'starttime','EndTime','Journey_type','stat',]
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        # s=validated_data
        # print(s['Categories'])
        # Categories=CategoriesSerializer(data=s)
        # if Categories.is_valid():
        #     Categories.save()

        return trip.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
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
        # instance.Categories = validated_data.get('Categories', instance.Categories)
        # # instance.Categories=CategoriesSerializer.update(instance,validated_data)
        # instance.client = validated_data.get('client', instance.client)
        # instance.driver = validated_data.get('driver', instance.driver)

        instance.save()
        return instance
