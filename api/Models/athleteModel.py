from django.db import models
from .asociationModel import Asociation
from .teamModel import Team


class Athlete(models.Model):
    athlete_name = models.CharField(max_length=40, blank=False, default='')
    biography = models.TextField(max_length=700, blank=True)
    wins = models.IntegerField(blank=False, default=0)
    loses = models.IntegerField(blank=False, default=0)
    games = models.IntegerField(blank=False, default=0)
    contact = models.CharField(max_length=200, blank=True)
    asociation = models.ForeignKey(Asociation, null=True, blank=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    shirt_number = models.IntegerField(blank=False, default=99)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    countries = [
        ('Guatemala', 'Guatemala'),
        ('El Salvador', 'El Salvador'),
        ('Honduras', 'Honduras'),
        ('Nicaragua', 'Nicaragua'),
        ('Costa Rica', 'Costa Rica'),
        ('Panamá', 'Panamá'),
        ('México', 'México')
    ]
    country = models.CharField(max_length=32, choices=countries, blank=False, default='Guatemala')

    def __str__(self):
        return self.athlete_name
