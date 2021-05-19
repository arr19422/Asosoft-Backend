
from rest_framework import viewsets
from ..Models.athleteModel import Athlete
from ..Serializers.athleteSerializer import AthleteSerializer


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
