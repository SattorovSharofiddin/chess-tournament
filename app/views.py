from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app.models import Player, Game
from app.serializers import PlayerSerializer, GameSerializer, GamePostSerializer


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

    def get_serializer_class(self):
        if self.action == 'create':
            return GamePostSerializer
        return GameSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        player = serializer.save()
        result = 'draw'
        color = 'white'

        if request.data['result'] == 'win':
            result = 'loss'
        elif request.data['result'] == 'loss':
            result = 'win'

        if request.data['color'] == 'white':
            color = 'black'

        Game.objects.create(
            result=result,
            color=color,
            number_of_moves=request.data['number_of_moves'],
            date_played=player.date_played,
            opening_type_id=request.data['opening_type'],
            player_id=request.data['rival_name'],
            rival_name_id=request.data['player']
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)
