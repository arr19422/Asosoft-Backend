from django.db import models
from .teamModel import Team
from .tournamentModel import Tournament
from .athleteModel import Athlete
from datetime import *


class Match(models.Model):
    match_date = models.DateField(blank=False)
    journey = models.IntegerField(blank=False, default=1)
    local_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False, related_name='local_team')
    visiting_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False, related_name='visiting_teams')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, blank=False)
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
    access_ticket = models.FloatField(blank=False, default=0)
    match_parking = models.TextField(max_length=300, blank=False, default='no')

    def __str__(self):
        return self.local_team.team_name + ' vs ' + self.visiting_team.team_name + ' | ' + str(self.match_date)
