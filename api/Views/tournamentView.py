from django.shortcuts import render
from rest_framework import viewsets
from ..serializers import *
from ..Models.tournamentModel import Tournament


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
