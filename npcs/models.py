from django.db import models
from django.utils import timezone


class MonsterType(models.Model):
    name = models.CharField(max_length=100)
    fightable = models.BooleanField(default=True)
    xp = models.IntegerField(null=True, blank=True)
    hit_points = models.IntegerField(null=True, blank=True)
    size = models.SmallIntegerField(
        choices=(
            (10, 'tiny'),
            (20, 'small'),
            (30, 'medium'),
            (40, 'large'),
            (50, 'huge'),
        )
    )
    common_drops = models.ManyToManyField('items.Item', related_name='drops_common')
    uncommon_drops = models.ManyToManyField('items.Item', related_name='drops_uncommon')
    rare_drops = models.ManyToManyField('items.Item', related_name='drops_rare')

    def __str__(self):
        return self.name


class Monster(models.Model):
    monster_type = models.ForeignKey(MonsterType)
    created = models.DateTimeField(default=timezone.now)

    @property
    def drops(self):
        """This function will return the items dropped once items are implemented"""
        drops = []
        return None
