from django.shortcuts import render
from rest_framework import viewsets
from ..Models.userModel import Users
from ..Serializers.userSerializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
