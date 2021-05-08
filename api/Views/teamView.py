from django.shortcuts import render
from rest_framework import viewsets
from ..Models.teamModel import Team
from ..Serializers.teamSerializer import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
