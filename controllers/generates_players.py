from models.players import Player
from random import randint


def generates_players():  # --> controllers
    """User enters informations of 8 players. returns list of 8 players"""
    players = []
    for player in range(1, 9):
        print(f"\nEntrez les informations du joueur {player} :\n ")
        player_id = player
        name = f"joueur "  # input("Nom : ")
        first_name = str(player)  # input("Prénom : ")
        birth = "01/01/2000"  # input("Date de naissance : ")
        sex = "m"  # input("Sexe : ")
        rank = randint(1, 50)  # int(input("Classement : "))

        player = Player(player_id, name, first_name, birth, sex, rank)
        players.append(player.serialize_player())
    # with open('players.json', "w", encoding='utf-8') as f:
    #     json.dump(players, f, indent=4, ensure_ascii=False)
    return players
