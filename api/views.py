from django.shortcuts import render
from .serializers import  EmployeeSerializer
from user.models import User
from rest_framework.viewsets import ModelViewSet 
from rest_framework import serializers, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import Employe

from rest_framework.throttling import UserRateThrottle
from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from knox.models import AuthToken
from api.serializers import CreateUserSerializer, GetUserSerializer
from django.contrib.auth import login


class CreateUserAPI(GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":GetUserSerializer(user, context=self.get_serializer_context()).data,
            "token": str(AuthToken.objects.create(user))
        })


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class OncePerDayUserThrottle(UserRateThrottle):
    rate = '5/day'


class EmpView(ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeeSerializer
    # throttle_classes = OncePerDayUserThrottle
    permission_classes = [
        permissions.AllowAny
    ]