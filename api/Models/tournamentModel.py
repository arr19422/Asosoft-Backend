from django.db import models
from datetime import *
from ..Models.teamModel import Team


class Tournament(models.Model):
    name = models.CharField(max_length=32, blank=False)
    category = models.CharField(max_length=32, blank=False, default="")
    tournament_logo = models.URLField(blank=False, default='')
    country = models.CharField(max_length=32, blank=False, default='Guatemala')
    current_date = models.IntegerField(blank=False, default=0)
    total_dates = models.IntegerField(blank=False, default=0)
    start_date = models.DateField(blank=False, default=datetime.now)
    end_date = models.DateField(blank=False, default=datetime.now)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.name
