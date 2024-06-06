import os
import random
import django

from faker import Faker
from app.models import Player, Country, Game, OpeningType

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

    for i in range(10):
        country = Country.objects.create(name=fake.country())
        countries.append(country)
    print('Fake country data created successfully!')

    for _ in range(100):
        rival = get_random_player()
        player = Player(
            name=fake.name(),
            country=random.choice(countries),
            wins=fake.random_int(0, 10),
            losses=fake.random_int(0, 10),
            draws=fake.random_int(0, 10),
            rival_name=rival,
        )
        player.save()
        players.append(player)
    print('Fake player data created successfully!')

    opening_types = []
    for i in range(10):
        opening_type = OpeningType.objects.create(name=fake.word())
        opening_types.append(opening_type)
    print('Fake Opening type data created successfully!')

    for _ in range(5000):
        white_player = get_random_player()
        black_player = get_random_player()

        if white_player and black_player:
            game = Game(
                result=random.choice(['win', 'loss', 'draw']),
                number_of_moves=fake.random_int(10, 100),
                date_played=fake.date_this_year(),
                white_player=white_player,
                black_player=black_player,
                opening_type=random.choice(opening_types)
            )
            game.save()
    print('Fake game data created successfully!')


if __name__ == "__main__":
    create_fake_data()
