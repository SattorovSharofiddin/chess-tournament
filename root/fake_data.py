import os
import random
import django
from faker import Faker
from app.models import Player, Country, Game, OpeningType

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
django.setup()

fake = Faker()


def get_random_player():
    players = list(Player.objects.all())
    if players:
        return random.choice(players)
    return None


def create_fake_data():
    countries = []
    players = []

    # Create fake countries
    for i in range(10):
        country = Country.objects.create(name=fake.country())
        countries.append(country)
    print('Fake country data created successfully!')

    # Create fake players
    for _ in range(100):
        player = Player(
            name=fake.name(),
            country=random.choice(countries)
        )
        player.save()
        players.append(player)
    print('Fake player data created successfully!')

    # Create fake opening types
    opening_types = []
    for i in range(10):
        opening_type = OpeningType.objects.create(name=fake.word())
        opening_types.append(opening_type)
    print('Fake opening type data created successfully!')

    # Create fake games
    for _ in range(5000):
        player = get_random_player()
        rival = get_random_player()

        if player and rival and player != rival:
            game = Game(
                result=random.choice([choice[0] for choice in Game.ChoiceResult.choices]),
                color=random.choice([choice[0] for choice in Game.ChoiceColor.choices]),
                number_of_moves=fake.random_int(10, 100),
                date_played=fake.date_this_year(),
                opening_type=random.choice(opening_types),
                player=player,
                rival_name=rival,
            )
            game.save()
    print('Fake game data created successfully!')


if __name__ == "__main__":
    create_fake_data()
