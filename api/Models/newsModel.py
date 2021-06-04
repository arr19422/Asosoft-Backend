from django.db import models
from ..Models.asociationModel import Asociation


class News(models.Model):
    news_title = models.CharField(max_length=32, blank=False)
    news_preview = models.TextField(max_length=50, blank=False)
    news_description = models.TextField(max_length=1000, blank=False)
    news_image = models.FileField(null=True)
    association = models.ForeignKey(Asociation, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.news_title


