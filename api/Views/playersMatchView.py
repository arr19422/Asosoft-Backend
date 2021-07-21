from rest_framework import viewsets
from ..Models.playersMatchModel import PlayersMatch
from ..Serializers.playersMatchSerializer import *
from rest_framework.decorators import action
from rest_framework.response import Response


class PlayersMatchViewSet(viewsets.ModelViewSet):
    queryset = PlayersMatch.objects.all()
    serializer_class = PlayersMatchSerializer

    @action(detail=False, methods=['GET'])
    def athlete_matches(self, request):
        athlete_id = request.GET.get('athlete_id')
        queryset = PlayersMatch.objects.filter(athlete__pk=athlete_id)
        serializer = PlayersMatchSerializer(queryset, many=True)
        return Response(serializer.data)
