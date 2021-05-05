from django.db import models
from .teamModel import Team
from .tournamentModel import Tournament


class Match(models.Model):
    match_date = models.DateField(blank=False)
    local_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False, related_name='local_teams')
    visiting_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False, related_name='visiting_teams')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return (self.local_team + ' vs ' + self.visiting_team)
