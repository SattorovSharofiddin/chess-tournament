from rest_framework import serializers
from app.models import Player, Game, OpeningType


class OpeningTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningType
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'country', 'game_count', 'total_points', 'elo_rating')

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     if instance.games.count() > 0:
    #         data['games'] = GameSerializer(instance.games, many=True).data
    #     return data


class GamePostSerializer(serializers.ModelSerializer):
    # date_played = serializers.DateTimeField(required=False)

    class Meta:
        model = Game
        fields = ('result', 'color', 'number_of_moves', 'date_played', 'opening_type', 'player', 'rival_name')


class GameSerializer(serializers.ModelSerializer):
    opening_type = serializers.PrimaryKeyRelatedField(queryset=OpeningType.objects.all())
    start_date = serializers.DateField(write_only=True)
    end_date = serializers.DateField(write_only=True)

    class Meta:
        model = Game
        fields = ('id', 'result', 'color', 'number_of_moves', 'date_played', 'opening_type', 'start_date', 'end_date')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['player'] = instance.player.name
        data['rival_name'] = instance.rival_name.name
        return data
