from django.db import models
from django.contrib.auth.models import User
from .asociationModel import Asociation
from .athleteModel import Athlete
from .teamModel import Team


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, default=None)
    #name = models.CharField(max_length=30, blank=False, default=None)
    #email = models.EmailField(blank=False, default=None)
    asociation = models.OneToOneField(Asociation, on_delete=models.CASCADE, blank=True, null=True,
                                      related_name="user_asociation")
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name="user_athlete")

    def __str__(self):
        return self.user
