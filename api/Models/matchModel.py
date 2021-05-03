from django.db import models
from .teamModel import Team
from .tournamentModel import Tournament


class Match(models.Model):
    match_date = models.DateField(blank=False)
    local_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False)
    visiting_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, blank=False)
