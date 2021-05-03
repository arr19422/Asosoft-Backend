from django.shortcuts import render
from rest_framework import viewsets
from ..serializers import *
from ..Models.matchModel import Match


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
