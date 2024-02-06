# serializers.py

from rest_framework import serializers

from .models import UserList, BMI



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = '__all__'

class BMISerializer(serializers.ModelSerializer):
    class Meta:
        model = BMI
        fields = ['bmi_value', 'classification']
