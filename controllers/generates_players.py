from models.player import Player
from random import randint


def enters_player_info(db):
    """Writes information of the new players entered by user in 'players.json' file"""
    print(f"\n\tEntrez les informations du joueur {len(db) + 1} :\n ")
    player_id = len(db) + 1
    name = input("Nom : ")
    first_name = input("Prénom : ")
    birth = input("Date de naissance : ")
    sex = input("Sexe : ")
    rank = randint(1, 200)
    total_score = 0
    player = Player(player_id, name, first_name, birth, sex, rank, total_score)
    print(f"\n\t*** {player.first_name} {player.name} a bien ajouté à la base de données ***")
    player.add_player_to_db()


def generates_players(id_player):
    """User enters information of 8 players. returns list of 8 players"""
    players = []
    for i in range(1, 9):
        print(f"\n\tEntrez les informations du joueur {id_player + i} :\n ")
        player_id = id_player + i
        name = "Joueur"  # input("Nom : ")
        first_name = str(id_player + i)  # input("Prénom : ")
        birth = "01/01/2000"  # input("Date de naissance : ")
        sex = "m"  # input("Sexe : ")
        rank = randint(1, 200)  # int(input("Classement : "))
        total_score = 0

        player = Player(player_id, name, first_name, birth, sex, rank, total_score)
        player.add_player_to_db()
        players.append(player.serialize_player)

    return players
