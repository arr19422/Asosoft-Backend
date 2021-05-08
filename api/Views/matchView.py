from django.shortcuts import render
from rest_framework import viewsets
from ..Models.matchModel import Match
from ..Serializers.matchSerializer import MatchSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
