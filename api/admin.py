from django.contrib import admin
from django.apps import apps
from .Models.matchModel import Match
from .Models.teamModel import Team
from .Models.tournamentModel import Tournament
from .Models.asociationModel import Asociation
from .Models.athleteModel import Athlete
from .Models.userModel import Users

admin.site.site_header = 'ASOSOFT Admin'
admin.site.site_title = 'Administracion de ASOSOFT App'
admin.site.index_title = 'Administracion'


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    fields = ['user', 'asociation', 'athlete']


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    fields = ['match_date', 'local_team', 'visiting_team', 'tournament', 'start_time', 'end_time', 'match_place',
              'facebook_link', 'youtube_link', 'local_score', 'visiting_score', 'match_type', 'access_ticket']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fields = ['team_name', 'team_description']


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'tournament_logo', 'country', 'current_date', 'total_dates', 'start_date', 'end_date',
              'teams']


@admin.register(Asociation)
class AsociationAdmin(admin.ModelAdmin):
    fields = ['name', 'photo']


@admin.register(Athlete)
class AthletAdmin(admin.ModelAdmin):
    fields = ['biography', 'wins', 'loses', 'games', 'contact', 'asociation', 'team']


