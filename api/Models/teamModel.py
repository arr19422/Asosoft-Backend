from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=32, blank=False)
    team_description = models.TextField(max_length=100, blank=False)

    def __str__(self):
        return self.team_name
