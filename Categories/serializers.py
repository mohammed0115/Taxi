# from django.contrib.auth.models import  Group
from rest_framework import serializers
# from Basic_salary.models import Temp_Employee

from rest_framework import serializers
from Categories.models import Categories
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields =['id','name','price']
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        print(validated_data)
        return Categories.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
   