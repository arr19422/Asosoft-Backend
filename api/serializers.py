from rest_framework import serializers
from .Models.matchModel import Match
from .Models.teamModel import Team
from .Models.tournamentModel import Tournament
from .Models.userModel import Users


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'match_date', 'local_team', 'visiting_team', 'tournament']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_name', 'team_description']


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'last_name', 'email', 'team']
