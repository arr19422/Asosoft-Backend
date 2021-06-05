from rest_framework import serializers
from ..Models.playersMatchModel import PlayersMatch

class PlayersMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersMatch
        fields = ['id', 'match_played', 'team', 'athlete']
        depth = 1
