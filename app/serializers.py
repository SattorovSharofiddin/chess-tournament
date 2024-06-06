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
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    rival_name = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(), allow_null=True)

    class Meta:
        model = Player
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    white_player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())
    black_player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())
    opening_type = serializers.PrimaryKeyRelatedField(queryset=OpeningType.objects.all())

    class Meta:
        model = Game
        fields = '__all__'
