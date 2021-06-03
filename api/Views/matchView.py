from django.shortcuts import render
from rest_framework import viewsets
from ..Models.matchModel import Match
from ..Serializers.matchSerializer import *
from rest_framework.decorators import action
import datetime
from rest_framework.response import Response


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    @action(detail=False, methods=['GET'])
    def past_matches(self, request):
        tournament_id = request.GET.get('event_id', 2)
        today = datetime.datetime.today()
        queryset = Match.objects.filter(match_date__lt=today).values('id', 'local_team', 'visiting_team', 'match_date', 'local_score',
                                                 'visiting_score', 'start_time')
        serializer = PastMatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def prueba(self, request):
        tournament_id = request.GET.get('event_id')
        today = datetime.datetime.today()
        queryset = Match.objects.filter(match_date__lt=today).filter(tournament__pk=tournament_id)\
            .values('id', 'match_date', 'local_score', 'visiting_score', 'start_time')
        serializer = PastMatchSerializer(queryset, many=True)
        return Response(serializer.data)
