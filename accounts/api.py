from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users ("players") to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer