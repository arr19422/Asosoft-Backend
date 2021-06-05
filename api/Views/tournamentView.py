from django.shortcuts import render
from rest_framework import viewsets
from ..Models.tournamentModel import Tournament
from ..Serializers.tournamentSerializer import *
from rest_framework.decorators import action
import datetime
from rest_framework.response import Response
from django.db.models import Q


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    @action(detail=False, methods=['GET'])
    def past_events(self, request):
        association_id = request.GET.get('association_id')
        today = datetime.datetime.today()
        queryset = Tournament.objects.filter(end_date__lt=today).filter(association=association_id)\
            .values('id', 'tournament_name', 'tournament_category', 'tournament_winner', 'end_date')\
            .order_by('end_date')
        serializer = PastTournamentSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def current_events(self, request):
        association_id = request.GET.get('association_id')
        today = datetime.datetime.today()
        criterion1 = Q(start_date__lte=today)
        criterion2 = Q(end_date__gte=today)
        queryset = Tournament.objects.filter(criterion1 & criterion2).filter(association=association_id)\
            .values('id', 'tournament_name', 'tournament_category', 'current_date', 'total_dates', 'end_date')\
            .order_by('start_date')
        serializer = CurrentTournamentSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def future_events(self, request):
        association_id = request.GET.get('association_id')
        today = datetime.datetime.today()
        queryset = Tournament.objects.filter(start_date__gt=today).filter(association=association_id)\
            .values('id', 'tournament_name', 'tournament_category', 'tournament_country', 'start_date')\
            .order_by('-start_date')
        serializer = FutureTournamentSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def event_info(self, request):
        event_id = request.GET.get('event_id')
        queryset = Tournament.objects.filter(id=event_id)
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)
