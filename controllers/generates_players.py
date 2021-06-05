import os
from models.player import Player
from tinydb import TinyDB
from views.art import display_players_art
from views.menu import display_add_player_menu, choose_item
from views.reports import players_reports
from controllers.press_to_clear import enter_to_clear
from controllers.confirm import confirm_action

players_db = TinyDB('players.json', encoding='utf-8', ensure_ascii=False, indent=4)


def player_information(player_id):
    name = input("Nom : ")
    first_name = input("Prénom : ")
    birth = input("Date de naissance : ")
    sex = input("Sexe : ")
    rank = int(input("Classement : "))
    total_score = 0
    player = Player(player_id, name, first_name, birth, sex, rank, total_score)
    return player


def enters_player_info():
    """Writes information of the new players entered by user in 'players.json' file"""
    print(f"\n\tEntrez les informations du joueur {len(players_db) + 1} :\n ")
    player_id = len(players_db) + 1
    player = player_information(player_id)
    print(f"\n\t*** {player.first_name} {player.name} a bien été ajouté(e) à la base de données ***")
    player.add_player_to_db()


def generates_players(id_player):
    """User enters information of 8 players. returns list of 8 players"""
    players = []
    for i in range(1, 9):
        print("\n\tEntrez les informations du nouveau joueur:\n")
        player_id = id_player + i
        player = player_information(player_id)
        player.add_player_to_db()
        players.append(player.serialize_player)
    return players


def add_player_from_db():
    """
    User can choose to add a player from db or to add him manually. returns a list of 8 players
    """
    players = []
    while not len(players) == 8:
        serialized_players = players_db.all()
        os.system('cls')
        print(display_players_art)
        print(f"\n\t\t*** Vous devez ajouter {8 - len(players)} joueur(s) ***\n")
        print("\t    Joueurs inscrits :\n")

        for i in range(len(players)):
            player_firstname = players[i]['first_name']
            player_name = players[i]['name']
            print(f"\t\t|  - {player_firstname} {player_name}")
        display_add_player_menu()
        user_choice = choose_item(3)

        # add player from db
        if user_choice == 1:
            os.system('cls')
            print(display_players_art)
            players_reports(1, serialized_players)
            print("\n\tEntrez l'identifiant du joueur à ajouter au tournoi\n")
            user_choice_2 = 0
            player_id_list = []

            # creates a list which contains players'ids of players added to tournament
            for i in range(len(players)):
                player_id_list.append(players[i]['player_id'])
            while True:
                try:
                    user_choice_2 = choose_item(len(serialized_players))
                    if user_choice_2 not in player_id_list:
                        break
                except ValueError:
                    print("\n\t\t *** Le joueur est déjà ajouté au tournoi ***")
                    enter_to_clear()
                    continue

            players.append(serialized_players[user_choice_2 - 1])
            player_firstname = serialized_players[user_choice_2 - 1]['first_name']
            player_name = serialized_players[user_choice_2 - 1]['name']
            os.system('cls')
            print(f"\n\t*** {player_firstname} {player_name} a été ajouté(e) au tournoi ***")
            enter_to_clear()

        # add a new player manually
        elif user_choice == 2:
            enters_player_info()
            serialized_players = players_db.all()
            players.append(serialized_players[-1])
            print("\n\t\t *** Ajout du joueur au Tournoi ***")
            enter_to_clear()
        elif user_choice == 3:
            if confirm_action() == 1:
                players = []
                os.system('cls')
                return players
            else:
                continue
    return players
