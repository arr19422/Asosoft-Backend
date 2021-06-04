
from rest_framework import viewsets
from ..Models.newsModel import News
from ..Serializers.newsSerializer import *
from rest_framework.decorators import action
from rest_framework.response import Response


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(detail=False, methods=['GET'])
    def association_news(self, request):
        association_id = request.GET.get('association_id')
        queryset = News.objects.filter(association=association_id)
        serializer = GeneralNewsSerializer(queryset, many=True)
        return Response(serializer.data)
