from django.db import models
from django.contrib.auth.models import AbstractUser
from .teamModel import Team


class Users(AbstractUser):
    name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length=32, blank=False)
    email = models.CharField(max_length=32, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False)