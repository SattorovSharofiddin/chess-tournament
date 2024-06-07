from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)


class Player(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    @property
    def game_count(self):
        return self.games.count()

    @property
    def total_points(self):
        return self.games.filter(result='win').count() * 2 + self.games.filter(result='draw').count()


class OpeningType(models.Model):
    name = models.CharField(max_length=100)


class Game(models.Model):
    class ChoiceResult(models.TextChoices):
        WIN = 'win', 'Win'
        LOSS = 'loss', 'Loss'
        DRAW = 'draw', 'Draw'

    class ChoiceColor(models.TextChoices):
        WHITE = 'white', 'White'
        BLACK = 'black', 'Black'

    result = models.CharField(max_length=10, choices=ChoiceResult.choices)
    color = models.CharField(max_length=5, choices=ChoiceColor.choices)

    number_of_moves = models.IntegerField()
    date_played = models.DateTimeField(auto_now_add=True)

    opening_type = models.ForeignKey(OpeningType, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, related_name='games', on_delete=models.CASCADE)
    rival_name = models.ForeignKey(Player, on_delete=models.CASCADE)
