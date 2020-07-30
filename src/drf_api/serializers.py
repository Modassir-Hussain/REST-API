from rest_framework import serializers, status
from drf_api.models import Employee
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class EmployeeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
       


