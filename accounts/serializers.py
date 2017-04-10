from .models import Player
from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'username',
            'email',
            'xp',
            'level',
        )