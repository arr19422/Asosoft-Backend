from rest_framework import serializers
from ..Models.newsModel import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'news_title', 'news_preview', 'news_description', 'news_image', 'association']


class GeneralNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'news_title', 'news_preview', 'news_image']