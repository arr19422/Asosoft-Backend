from rest_framework import serializers
from ..Models.athleteModel import Athlete


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ['id', 'athlete_name', 'biography', 'wins', 'loses', 'games', 'contact', 'asociation', 'team', 'shirt_number']