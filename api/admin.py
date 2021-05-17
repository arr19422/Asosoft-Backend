from django.contrib import admin
from django.apps import apps
from .Models.matchModel import Match
from .Models.teamModel import Team
from .Models.tournamentModel import Tournament

admin.site.site_header = 'ASOSOFT Admin'
admin.site.site_title = 'Administracion de ASOSOFT App'
admin.site.index_title = 'Administracion'


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    fields = ['match_date', 'local_team', 'visiting_team', 'tournament']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fields = ['team_name', 'team_description']


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    fields = ['name']


"""
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
"""
