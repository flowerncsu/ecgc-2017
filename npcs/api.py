from rest_framework import viewsets
from .models import Character, CharacterType
from .serializers import CharacterSerializer, CharacterTypeSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows characters to be viewed or edited.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows character types to be viewed or edited.
    """
    queryset = CharacterType.objects.all()
    serializer_class = CharacterTypeSerializer
