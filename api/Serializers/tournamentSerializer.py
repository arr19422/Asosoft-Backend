from rest_framework import serializers
from ..Models.tournamentModel import Tournament


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'tournament_name', 'tournament_category', 'tournament_country', 'tournament_winner',
                  'current_date', 'total_dates', 'start_date', 'end_date', 'teams']