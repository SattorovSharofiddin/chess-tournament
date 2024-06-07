from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app.filters import PlayerFilter
from app.models import Player, Game
from app.serializers import PlayerSerializer, GameSerializer, GamePostSerializer


class PlayerList(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    parser_classes = FormParser, MultiPartParser
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlayerFilter

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY, description="Name (icontains)", type=openapi.TYPE_STRING),
            openapi.Parameter('elo_rating_min', openapi.IN_QUERY, description="Minimum ELO rating",
                              type=openapi.TYPE_NUMBER),
            openapi.Parameter('elo_rating_max', openapi.IN_QUERY, description="Maximum ELO rating",
                              type=openapi.TYPE_NUMBER),
            openapi.Parameter('country', openapi.IN_QUERY, description="Country (icontains)", type=openapi.TYPE_STRING),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class GameList(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    parser_classes = FormParser, MultiPartParser
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        if self.action == 'create':
            return GamePostSerializer
        elif self.action == 'list':
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

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Start date for filtering games",
                              type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="End date for filtering games",
                              type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
        ]
    )
    def list(self, request, *args, **kwargs):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        start_date += 'T00:00:00Z'
        end_date += 'T23:59:59Z'
        if start_date and end_date:
            self.queryset = self.queryset.filter(date_played__range=[start_date, end_date])
        if self.request.query_params.get('result'):
            self.queryset = self.queryset.filter(result=self.request.query_params.get('result'))
        if self.request.query_params.get('opening_type'):
            self.queryset = self.queryset.filter(opening_type=self.request.query_params.get('opening_type'))
        if self.request.query_params.get('player'):
            self.queryset = self.queryset.filter(player=self.request.query_params.get('player'))
        return super().list(request, *args, **kwargs)
