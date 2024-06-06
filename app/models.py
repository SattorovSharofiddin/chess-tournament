from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Country(models.Model):
    name = models.CharField(max_length=100)


class Player(MPTTModel):
    name = models.CharField(max_length=100)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    rival_name = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='rivals')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    @property
    def game_count(self):
        return self.white_games.count() + self.black_games.count()

    @property
    def total_points(self):
        return (self.white_games.filter(result='win').count() * 2) + (
                self.black_games.filter(result='win').count() * 2) + (
                self.white_games.filter(result='draw').count() * 1) + (
                self.black_games.filter(result='draw').count() * 1)


class OpeningType(models.Model):
    name = models.CharField(max_length=100)


class Game(models.Model):
    class ChoiceField(models.TextChoices):
        WIN = 'win', 'Win'
        LOSS = 'loss', 'Loss'
        DRAW = 'draw', 'Draw'

    result = models.CharField(max_length=10, choices=ChoiceField.choices)

    number_of_moves = models.IntegerField()
    date_played = models.DateTimeField(auto_now_add=True)

    white_player = models.ForeignKey(Player, related_name='white_games', on_delete=models.CASCADE)
    black_player = models.ForeignKey(Player, related_name='black_games', on_delete=models.CASCADE)
    opening_type = models.ForeignKey(OpeningType, on_delete=models.CASCADE)
