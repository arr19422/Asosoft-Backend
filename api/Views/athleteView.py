
from rest_framework import viewsets
from ..Models.athleteModel import Athlete
from ..Serializers.athleteSerializer import AthleteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer

    @action(detail=False, methods=['GET'])
    def match_players(self, request):
        local_id = request.GET.get('local_id')
        visiting_id = request.GET.get('visiting_id')
        local_players = Athlete.objects.filter(team=local_id)
        visiting_players = Athlete.objects.filter(team=visiting_id)
        response = {'local_team': {}, 'visiting_team': {}}
        for i in local_players:
            response['local_team'][i.athlete_name] = i.shirt_number
        for i in visiting_players:
            response['visiting_team'][i.athlete_name] = i.shirt_number
        return Response(response)

