from django.contrib import admin
from django.apps import apps
from .Models.matchModel import Match
from .Models.teamModel import Team
from .Models.tournamentModel import Tournament
from .Models.asociationModel import Asociation
from .Models.athleteModel import Athlete
from .Models.userModel import Users
from .Models.newsModel import News
from .Models.playersMatchModel import PlayersMatch

admin.site.site_header = 'ASOSOFT Admin'
admin.site.site_title = 'Administracion de ASOSOFT App'
admin.site.index_title = 'Administracion'


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    fields = ['user', 'asociation', 'athlete']


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    fields = ['match_date', 'journey', 'local_team', 'visiting_team', 'tournament', 'start_time',
              'end_time', 'match_place', 'facebook_link', 'youtube_link', 'local_score', 'visiting_score',
              'match_type', 'access_ticket', 'match_parking']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fields = ['team_name', 'team_description', 'team_image']


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    fields = ['tournament_name', 'tournament_category', 'tournament_country', 'tournament_winner',
                  'current_date', 'total_dates', 'start_date', 'end_date', 'teams', 'association']


@admin.register(Asociation)
class AsociationAdmin(admin.ModelAdmin):
    fields = ['name', 'photo']


@admin.register(Athlete)
class AthletAdmin(admin.ModelAdmin):
    fields = ['athlete_name', 'biography', 'wins', 'loses', 'games', 'contact', 'asociation', 'team',
              'shirt_number', 'instagram', 'facebook', 'email', 'country']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ['news_title', 'news_preview', 'news_description', 'news_image', 'association']


@admin.register(PlayersMatch)
class PlayersMatchAdmin(admin.ModelAdmin):
    fields = ['match_played', 'team', 'athlete']


