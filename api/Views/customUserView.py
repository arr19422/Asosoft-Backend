from django.shortcuts import render
from rest_framework import viewsets
from ..Models.userModel import Users
from ..Serializers.customUserSerializer import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = CustomUserSerializer
