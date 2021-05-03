from django.shortcuts import render
from rest_framework import viewsets
from ..serializers import *
from ..Models.teamModel import Team


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
