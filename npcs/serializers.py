from .models import Monster, MonsterType
from rest_framework import serializers


class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = (
            'created',
            'id',
            'monster_type',
            'url',
        )


class MonsterTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonsterType
        fields = (
            'name',
            'fightable',
            'hit_points',
            'size',
            'url',
            'xp',
        )
