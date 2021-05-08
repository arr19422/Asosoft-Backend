from rest_framework import serializers
from ..Models.tournamentModel import Tournament


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'name']