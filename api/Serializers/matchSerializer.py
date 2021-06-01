from rest_framework import serializers
from ..Models.matchModel import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'match_date', 'journey', 'local_team', 'visiting_team', 'tournament', 'start_time',
                  'end_time', 'match_place', 'facebook_link', 'youtube_link', 'local_score', 'visiting_score',
                  'match_type', 'access_ticket', 'match_parking']
