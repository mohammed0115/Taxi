from django.contrib.auth.models import  Group
from rest_framework import serializers
# from Basic_salary.models import Temp_Employee

from rest_framework import serializers
# from Basic_salary.models import Temp_Employee

from rest_framework import serializers
from License.models import License
class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields ='__all__'
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return License.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.issueDate = validated_data.get('issueDate', instance.issueDate)
        instance.expDate = validated_data.get('expDate', instance.expDate)
        instance.License_type = validated_data.get('License_type', instance.License_type)
        instance.issuePlace = validated_data.get('issuePlace', instance.issuePlace)
        
        instance.save()
        return instance
   