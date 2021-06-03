from django.db import models
from datetime import *
from ..Models.teamModel import Team


class Tournament(models.Model):
    tournament_name = models.CharField(max_length=32, blank=False)
    tournament_category = models.CharField(max_length=32, blank=False, default="")
    tournament_country = models.CharField(max_length=32, blank=False, default='Guatemala')
    tournament_winner = models.OneToOneField(Team, on_delete=models.CASCADE, blank=True,
                                             related_name='tournament_winner', null=True)
    current_date = models.IntegerField(blank=False, default=0)
    total_dates = models.IntegerField(blank=False, default=0)
    start_date = models.DateField(blank=False, default=datetime.now)
    end_date = models.DateField(blank=False, default=datetime.now)
    teams = models.ManyToManyField(Team, related_name='teams')

    def __str__(self):
        return self.tournament_name + '|' + self.tournament_category
