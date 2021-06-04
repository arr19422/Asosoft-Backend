
from rest_framework import viewsets, status
from ..Models.asociationModel import Asociation
from ..Models.newsModel import News
from ..Models.tournamentModel import Tournament
from ..Models.matchModel import Match
from ..Serializers.asociationSerializer import AsociationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import datetime


class AsociationViewSet(viewsets.ModelViewSet):
    queryset = Asociation.objects.all()
    serializer_class = AsociationSerializer

    @action(detail=False, methods=['GET'])
    def associations_info(self, request):
        queryset = Asociation.objects.all()
        response = {}
        for i in queryset:
            sport_news = len(News.objects.filter(association=i))
            today = datetime.datetime.today()
            tournaments_list = Tournament.objects.filter(association_id=i.id)
            print(tournaments_list)
            sport_results = len(Match.objects.filter(match_date__lt=today).filter(tournament__in=tournaments_list))
            response[i.id] = {
                'sport': i.name,
                'photo': str(i.photo),
                'news': sport_news,
                'results': sport_results
            }
        return Response(response, status=status.HTTP_200_OK)