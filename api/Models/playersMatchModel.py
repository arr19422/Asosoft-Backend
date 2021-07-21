from django.db import models
from .matchModel import Match
from .teamModel import Team
from .athleteModel import Athlete


class PlayersMatch(models.Model):
    match_played = models.ForeignKey(Match, on_delete=models.CASCADE, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=False, related_name='athletes')

    def __str__(self):
        return str(self.match_played.match_date) + ' | ' + self.team.team_name + ' | ' + self.athlete.athlete_name
