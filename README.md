![Screenshot from 2024-06-07 18-35-41](https://github.com/SattorovSharofiddin/chess-tournament/assets/82801130/76dcf0d2-e1a3-463f-8950-c85b24f336f6)


Here's the database structure:

plaintext
Копировать код
Country:
- id (PK)
- name (CharField)

Player:
- id (PK)
- name (CharField)
- country_id (FK to Country)
- elo_rating (IntegerField)

OpeningType:
- id (PK)
- name (CharField)

Game:
- id (PK)
- result (CharField)
- color (CharField)
- number_of_moves (IntegerField)
- date_played (DateTimeField)
- opening_type_id (FK to OpeningType)
- player_id (FK to Player)
- rival_name_id (FK to Player)
Explanation:

Country: Stores information about countries.
Player: Stores information about players, including their name, country, and elo rating.
OpeningType: Stores information about different types of openings.
Game: Stores information about each game played, including result, color, number of moves, date played, and references to the player, rival player, and opening type.
PK = Primary Key
FK = Foreign Key




![image](https://github.com/SattorovSharofiddin/chess-tournament/assets/82801130/e839119b-47ea-440f-b036-2cb21ca7ccc5)


3 API sections are available




![image](https://github.com/SattorovSharofiddin/chess-tournament/assets/82801130/23c50bf6-2f8b-4021-a454-10e7386cb4d7)


Api section related to the game




![image](https://github.com/SattorovSharofiddin/chess-tournament/assets/82801130/326a5275-e30d-4ff2-90a0-19c85921133b)



Api section related to the players





![image](https://github.com/SattorovSharofiddin/chess-tournament/assets/82801130/c3700e7e-1c0a-43a4-bbfc-1af12b3106ef)


Section for updating ratings based on results




Data Generation:

Create a mechanism to generate up to 5,000 realistic chess game records, including information such as:
- Player names (white & black)
- Game result (win, loss, draw)
- Opening type (e.g., Sicilian Defense, Ruy Lopez)
- Number of moves
- Date played

Create player profiles with attributes like:
- Name
- Elo rating
- Country
- Number of games played
- Win/loss/draw statistics

Advanced Filtering:
Implement filtering capabilities on the REST API for both games and players. Allow filtering by:
- Player name
- Game result
- Opening type
- Date range
-Elo rating range
- Country

Integrate caching for players list


REST API:
- Design and implement a comprehensive REST API using Django REST Framework (DRF) to:
- Retrieve game records
- Retrieve player profiles
- Filter game and player data
- Add new game records (optionally)
- Update player ratings based on game outcomes (optionally)


