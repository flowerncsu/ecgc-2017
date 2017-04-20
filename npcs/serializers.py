from .models import Character, CharacterType
from rest_framework import serializers


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'created',
            'id',
            'character_type',
            'url',
        )


class CharacterTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterType
        fields = (
            'name',
            'fightable',
            'hit_points',
            'size',
            'url',
            'xp',
        )
