from django.contrib.auth.models import  Group
from rest_framework import serializers
# from Basic_salary.models import Temp_Employee

from rest_framework import serializers
from .models import user,driver,client
from License.models import License
from Vehicle.models import Vehicle
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




class LicenseSerializer(serializers.Serializer):
    License_type = serializers.CharField(max_length=50)
    
    class Meta:
        model=License

class VehicleSerializer(serializers.Serializer):
    chassNo = serializers.CharField(max_length=25)
    plateNo =serializers.IntegerField()
    color = serializers.CharField(max_length=20)
    model=serializers.CharField(max_length=90)
    year = serializers.IntegerField()
    class Meta:
        model=Vehicle



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']






class DriverSerializer(serializers.ModelSerializer):
    License=LicenseSerializer()
    Vehicle=VehicleSerializer()
    class Meta:
        model = driver
        fields =['id','phone','email','address', 'username',
        'date_of_birth','gender','Vehicle','lat','lon','status','bloodClass','License']
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        License_data = validated_data.pop('License')
        Vehicle_data = validated_data.pop('Vehicle')
        


        t = driver.objects.create(**validated_data)
        # print(Categories_data.get('name'))
        lic, created = License.objects.get_or_create(**License_data)
        vehicle,created  =Vehicle.objects.get_or_create(**Vehicle_data)
        t.License=lic
        t.Vehicle=vehicle
        t.save()
        
        return t


    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        License_data = validated_data.pop('License')
        Vehicle_data = validated_data.pop('Vehicle')


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

        lic, created = License.objects.get_or_create(**License_data)
        vehicle,created  =Vehicle.objects.get_or_create(**Vehicle_data)
        instance.License=lic
        instance.Vehicle=vehicle
        instance.save()
        return instance






class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields ='__all__'
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

