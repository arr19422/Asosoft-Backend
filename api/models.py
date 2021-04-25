from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=32, blank=False)
    team_description = models.TextField(max_length=100, blank=False)


class Users(AbstractUser):
    name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length=32, blank=False)
    email = models.CharField(max_length=32, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False)


class Tournament(models.Model):
    name = models.CharField(max_length=32, blank=False)


class Match(models.Model):
    match_date = models.DateField(blank=False)
    local_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False)
    visiting_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, blank=False)


