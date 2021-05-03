from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=32, blank=False)
