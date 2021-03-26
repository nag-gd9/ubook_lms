from rest_framework import serializers
from user.models import User
from .models import Employe
from django.contrib.auth import authenticate


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', ]


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employe
        fields = '__all__'