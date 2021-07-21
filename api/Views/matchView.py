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
        tournament_id = request.GET.get('event_id')
        today = datetime.datetime.today()
        queryset = Match.objects.filter(match_date__lt=today).filter(tournament__pk=tournament_id)
        serializer = PastMatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def next_matches(self, request):
        tournament_id = request.GET.get('event_id')
        today = datetime.datetime.today()
        queryset = Match.objects.filter(match_date__gt=today).filter(tournament__pk=tournament_id)
        serializer = PastMatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def upcoming_match(self, request):
        match_id = request.GET.get('match_id')
        queryset = Match.objects.filter(id=match_id)
        serializer = UpcomingMatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def finished_match(self, request):
        match_id = request.GET.get('match_id')
        queryset = Match.objects.filter(id=match_id)
        serializer = FinishedMatchSerializer(queryset, many=True)
        return Response(serializer.data)



