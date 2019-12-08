from django.contrib.auth.models import  Group
from rest_framework import serializers
# from Basic_salary.models import Temp_Employee

from rest_framework import serializers
# from Basic_salary.models import Temp_Employee

from rest_framework import serializers
from Vehicle.models import Vehicle
from Categories.serializers import CategoriesSerializer
class VehicleSerializer(serializers.ModelSerializer):
    Categories= CategoriesSerializer(many=True)
    class Meta:
        model = Vehicle
        fields =['id','chassNo','plateNo','color','model','year','Categories']
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return Vehicle.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.chassNo = validated_data.get('chassNo', instance.chassNo)
        instance.plateNo = validated_data.get('plateNo', instance.plateNo)
        instance.color = validated_data.get('color', instance.color)
        instance.model = validated_data.get('model', instance.model)
        instance.year = validated_data.get('year', instance.year)
        instance.Categories = validated_data.get('Categories', instance.Categories)

        
        instance.save()
        return instance
   