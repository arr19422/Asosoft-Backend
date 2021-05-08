from rest_framework import serializers
from ..Models.matchModel import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'match_date', 'local_team', 'visiting_team', 'tournament']