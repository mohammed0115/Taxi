from django.contrib.auth.models import  Group
from rest_framework import serializers
# from Basic_salary.models import Temp_Employee

from rest_framework import serializers
from .models import user,driver,client
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields =['phone','email','address', 'username','password',
        'date_of_birth','gender']
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return user.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.password = validated_data.get('password', instance.password)
        # instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.username = validated_data.get('username', instance.username)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        # instance.lat = validated_data.get('lat', instance.lat)
        instance.gender = validated_data.get('gender', instance.gender)
        # instance.log = validated_data.get('username', instance.log)
        # instance.status = validated_data.get('status', instance.status)
        # instance.bloodClass = validated_data.get('bloodClass', instance.bloodClass)
        # instance.License = validated_data.get('License', instance.License)
        # instance.Vehicle = validated_data.get('Vehicle', instance.Vehicle)
        instance.save()
        return instance










class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']






class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = driver
        fields =['phone',]
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return driver.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.password = validated_data.get('password', instance.password)
        # instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.username = validated_data.get('username', instance.username)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.lon = validated_data.get('lon', instance.lon)
        instance.status = validated_data.get('status', instance.status)
        instance.bloodClass = validated_data.get('bloodClass', instance.bloodClass)
        instance.License = validated_data.get('License', instance.License)
        instance.Vehicle = validated_data.get('Vehicle', instance.Vehicle)
        instance.save()
        return instance






class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields =['phone',]
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.password = validated_data.get('password', instance.password)
        # instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.username = validated_data.get('username', instance.username)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        # instance.lat = validated_data.get('lat', instance.lat)
        instance.gender = validated_data.get('gender', instance.gender)
        # instance.log = validated_data.get('username', instance.log)
        # instance.status = validated_data.get('status', instance.status)
        # instance.bloodClass = validated_data.get('bloodClass', instance.bloodClass)
        # instance.License = validated_data.get('License', instance.License)
        # instance.Vehicle = validated_data.get('Vehicle', instance.Vehicle)
        instance.save()
        return instance

