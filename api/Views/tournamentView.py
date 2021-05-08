from django.shortcuts import render
from rest_framework import viewsets
from ..Models.tournamentModel import Tournament
from ..Serializers.tournamentSerializer import TournamentSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
