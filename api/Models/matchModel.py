from django.db import models
from .teamModel import Team
from .tournamentModel import Tournament
from datetime import *


class Match(models.Model):
    match_date = models.DateField(blank=False)
    local_team = models.OneToOneField(Team, on_delete=models.CASCADE, blank=False, related_name='local_teams')
    visiting_team = models.OneToOneField(Team, on_delete=models.CASCADE, blank=False, related_name='visiting_teams')
    tournament = models.OneToOneField(Tournament, on_delete=models.CASCADE, blank=False)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, default=datetime.now)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, default=datetime.now)
    match_place = models.CharField(max_length=32, blank=False, default="")
    facebook_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)
    local_score = models.IntegerField(blank=False, default=0)
    visiting_score = models.IntegerField(blank=False, default=0)
    match_types = [
        ('Amistoso', 'Amistoso'),
        ('Torneo', 'Torneo'),
        ('Final', 'Final'),
        ('Internacional', 'Internacional')
    ]
    match_type = models.CharField(max_length=32, choices=match_types, blank=False, default='Torneo')
    access_ticket = models.DecimalField(blank=False, default=0, decimal_places=3, max_digits=4)

    def __str__(self):
        return self.local_team.team_name + ' vs ' + self.visiting_team.team_name + ' | ' + str(self.match_date)
