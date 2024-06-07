from rest_framework import serializers
from app.models import Player, Country, Game, OpeningType


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class OpeningTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningType
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'country', 'game_count', 'total_points')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.games.count() > 0:
            data['result'] = instance.games.result
            data['number_of_moves'] = instance.games.number_of_moves
            data['date_played'] = instance.games.date_played
            data['opening_type'] = instance.games.opening_type.name
            data['color'] = instance.games.color
            data['country'] = instance.country.name
            data['rival_name'] = instance.rival_name.name
            data['games'] = [game.id for game in instance.games.all()]
        return data


class GameSerializer(serializers.ModelSerializer):
    white_player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())
    black_player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())
    opening_type = serializers.PrimaryKeyRelatedField(queryset=OpeningType.objects.all())

    class Meta:
        model = Game
        fields = '__all__'
