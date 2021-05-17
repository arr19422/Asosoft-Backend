from django.db import models
from django.contrib.auth.models import AbstractUser, User
from .teamModel import Team


class Users(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default=None)

    def __str__(self):
        return self.user
