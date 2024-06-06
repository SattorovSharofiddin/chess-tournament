from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet

from app.models import Player, Game
from app.serializers import PlayerSerializer, GameSerializer


class PlayerList(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    parser_classes = FormParser, MultiPartParser
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name', 'total_points', 'country']


class GameList(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    parser_classes = FormParser, MultiPartParser
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['white_player__name', 'black_player__name', 'result', 'opening_type', 'date_played']
