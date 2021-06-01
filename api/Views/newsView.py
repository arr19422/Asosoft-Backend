
from rest_framework import viewsets
from ..Models.newsModel import News
from ..Serializers.newsSerializer import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
