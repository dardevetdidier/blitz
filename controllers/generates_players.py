from models.players import Player
from random import randint
from tinydb import TinyDB

players_db = TinyDB('players.json', encoding='utf-8', ensure_ascii=False)


def enters_player_info():
    print(f"\nEntrez les informations du joueur {len(players_db) + 1} :\n ")
    player_id = len(players_db) + 1
    name = f"joueur "  # input("Nom : ")
    first_name = str(len(players_db) + 1)  # input("Prénom : ")
    birth = "01/01/2000"  # input("Date de naissance : ")
    sex = "m"  # input("Sexe : ")
    rank = randint(1, 200)
    player = Player(player_id, name, first_name, birth, sex, rank)
    player.add_player_to_db(players_db)


def generates_players(id_player):
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

        player = Player(player_id, name, first_name, birth, sex, rank)
        player.add_player_to_db(players_db)
        players.append(player.serialize_player)

    return players


# def add_player_db(player):
#     """insert player in db db"""
#     players_db.insert(player.serialize_player)
