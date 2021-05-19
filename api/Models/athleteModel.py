from django.db import models
from .asociationModel import Asociation
from .teamModel import Team


class Athlete(models.Model):
    biography = models.TextField(max_length=200, blank=True)
    wins = models.IntegerField(blank=False, default=0)
    loses = models.IntegerField(blank=False, default=0)
    games = models.IntegerField(blank=False, default=0)
    contact = models.CharField(max_length=200, blank=True)
    asociation = models.OneToOneField(Asociation, null=True, blank=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.team_name
