from rest_framework import serializers
from ..Models.userModel import Users


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'user', 'asociation', 'athlete']