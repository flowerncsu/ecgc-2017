from rest_framework import viewsets
from .models import Monster, MonsterType
from .serializers import MonsterSerializer, MonsterTypeSerializer


class MonsterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows monsters to be viewed or edited.
    """
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer


class MonsterTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows monster types to be viewed or edited.
    """
    queryset = MonsterType.objects.all()
    serializer_class = MonsterTypeSerializer
