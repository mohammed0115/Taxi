from django.contrib.auth.models import  Group
from rest_framework import serializers
# from Basic_salary.models import Temp_Employee

from rest_framework import serializers
# from Basic_salary.models import Temp_Employee

from rest_framework import serializers
from Vehicle.models import Vehicle

from Categories.models import Categories
class CategoriesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField()
    class Meta:
        model=Categories

class VehicleSerializer(serializers.ModelSerializer):
    Categories= CategoriesSerializer()
    class Meta:
        model = Vehicle
        fields =['id','chassNo','plateNo','color','model','year','Categories']
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        Categories_data = validated_data.pop('Categories')
        t = Vehicle.objects.create(**validated_data)
        cat, created = Categories.objects.get_or_create(**Categories_data)
        t.Categories=cat
        t.save()
        return t

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        Categories_data = validated_data.pop('Categories')
        instance.chassNo = validated_data.get('chassNo', instance.chassNo)
        instance.plateNo = validated_data.get('plateNo', instance.plateNo)
        instance.color = validated_data.get('color', instance.color)
        instance.model = validated_data.get('model', instance.model)
        instance.year = validated_data.get('year', instance.year)
        cat, created = Categories.objects.get_or_create(**Categories_data)
        instance.Categories = cat

        
        instance.save()
        return instance
   