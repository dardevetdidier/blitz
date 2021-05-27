from models.players import Player
from random import randint


def enters_player_info(db):
    print(f"\nEntrez les informations du joueur {len(db) + 1} :\n ")
    player_id = len(db) + 1
    name = f"joueur "  # input("Nom : ")
    first_name = str(len(db) + 1)  # input("Prénom : ")
    birth = "01/01/2000"  # input("Date de naissance : ")
    sex = "m"  # input("Sexe : ")
    rank = randint(1, 200)
    total_score = 0
    player = Player(player_id, name, first_name, birth, sex, rank, total_score)

    player.add_player_to_db(db)


def generates_players(id_player, db):
    """User enters information of 8 players. returns list of 8 players"""
    players = []
    for i in range(1, 9):
        print(f"\nEntrez les informations du joueur {id_player + i} :\n ")
        player_id = id_player + i
        name = f"joueur "  # input("Nom : ")
        first_name = str(id_player + i)  # input("Prénom : ")
        birth = "01/01/2000"  # input("Date de naissance : ")
        sex = "m"  # input("Sexe : ")
        rank = randint(1, 200)  # int(input("Classement : "))
        total_score = 0

        player = Player(player_id, name, first_name, birth, sex, rank, total_score)
        player.add_player_to_db(db)
        players.append(player.serialize_player)

    return players
