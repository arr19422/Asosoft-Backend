
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .Views.userView import UserViewSet
from .Views.matchView import MatchViewSet
from .Views.teamView import TeamViewSet
from .Views.tournamentView import TournamentViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('matches', MatchViewSet)
router.register('teams', TeamViewSet)
router.register('tournaments', TournamentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
