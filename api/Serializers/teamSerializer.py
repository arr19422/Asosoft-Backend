from rest_framework import serializers
from ..Models.teamModel import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_name', 'team_description', 'team_image']