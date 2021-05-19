from rest_framework import serializers
from ..Models.asociationModel import Asociation


class AsociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asociation
        fields = ['id', 'name']