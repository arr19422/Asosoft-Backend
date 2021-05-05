from django.contrib import admin
from django.apps import apps
from .Models.matchModel import Match
from .Models.teamModel import Team
from .Models.tournamentModel import Tournament
from .Models.userModel import User

admin.site.site_header = 'ASOSOFT Admin'
admin.site.site_title = 'Administracion de ASOSOFT App'
admin.site.index_title = 'Administracion'



models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
