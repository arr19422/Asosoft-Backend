
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .Views.customUserView import CustomUserViewSet
from .Views.matchView import MatchViewSet
from .Views.teamView import TeamViewSet
from .Views.tournamentView import TournamentViewSet
from .Views.athleteView import AthleteViewSet
from .Views.asociationView import AsociationViewSet
from .Views.newsView import NewsViewSet
from .Views.playersMatchView import PlayersMatchViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('users', CustomUserViewSet)
router.register('matches', MatchViewSet)
router.register('teams', TeamViewSet)
router.register('tournaments', TournamentViewSet)
router.register('athletes', AthleteViewSet)
router.register('asociations', AsociationViewSet)
router.register('news', NewsViewSet)
router.register('players_match', PlayersMatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
