from rest_framework import serializers
from ..Models.tournamentModel import Tournament
from ..Serializers.teamSerializer import TeamSerializer


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'tournament_name', 'tournament_category', 'tournament_country', 'tournament_winner',
                  'current_date', 'total_dates', 'start_date', 'end_date', 'teams', 'association']


class PastTournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'tournament_name', 'tournament_category', 'tournament_winner', 'end_date']


class CurrentTournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'tournament_name', 'tournament_category', 'current_date', 'total_dates', 'end_date']


class FutureTournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'tournament_name', 'tournament_category', 'tournament_country', 'start_date']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'tournament_name', 'tournament_category', 'tournament_country', 'tournament_winner',
                  'current_date', 'total_dates', 'start_date', 'end_date', 'teams']
        depth = 1
