from rest_framework import serializers
from ..Models.matchModel import Match
from ..Serializers.teamSerializer import TeamSerializer


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'match_date', 'journey', 'local_team', 'visiting_team', 'tournament', 'start_time',
                  'end_time', 'match_place', 'facebook_link', 'youtube_link', 'local_score', 'visiting_score',
                  'match_type', 'access_ticket', 'match_parking']


class PastMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'match_date', 'local_score', 'visiting_score', 'start_time', 'visiting_team', 'local_team']
        depth = 1


class UpcomingMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'match_date', 'journey', 'local_team', 'visiting_team', 'tournament', 'start_time',
                  'end_time', 'match_place', 'facebook_link', 'youtube_link', 'access_ticket', 'match_parking']
        depth = 1


class FinishedMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'match_date', 'journey', 'local_team', 'visiting_team', 'tournament', 'start_time',
                  'end_time', 'match_place', 'facebook_link', 'youtube_link', 'local_score', 'visiting_score',
                  'match_type', 'access_ticket', 'match_parking']
        depth = 2
