from django.shortcuts import render
from rest_framework import viewsets
from ..serializers import *
from ..Models.userModel import Users


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
