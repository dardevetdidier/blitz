from prettytable import PrettyTable
from controllers import press_to_clear
import os


def t_to_load(table_obj, tournaments):
    """ prints a table of all tournaments. User choose a tournament. Returns the number of the tournament (int)"""

    for i in range(len(tournaments)):
        table_obj.add_row([i + 1,
                           tournaments[i]['name'],
                           tournaments[i]['date'],
                           tournaments[i]['location'],
                           len(tournaments[i]['rounds'])
                           ])

    print("\n\t\tTournois sauvegardés")
    print(f"\n{table_obj}")
    tournament_to_load = 0
    while True:
        try:
            tournament_to_load = int(input("\n    --> Choisissez le n° du tournoi : "))
            if tournament_to_load in range(1, len(tournaments) + 1):
                break
        except ValueError:
            continue

    table_obj.clear()
    return tournament_to_load


def players_reports(user_choice, players):
    """displays a table of players sorted by name or ranking"""
    p_table_players = PrettyTable()
    p_table_players.field_names = ["identifiant", "Nom", "Prénom", "Date de naissance",
                                   "Classement"]
    for i in range(len(players)):
        p_table_players.add_row([players[i]['player_id'],
                                 players[i]['name'],
                                 players[i]['first_name'],
                                 players[i]['birth'],
                                 (players[i]['rank'])
                                 ])
    if user_choice == 1:
        p_table_players.sortby = "Nom"
        print("\t\t   Joueurs (par ordre alphabétique)")
    elif user_choice == 2:
        p_table_players.sortby = "Classement"
        print("\t\t       Joueurs (par classement)")

    print(p_table_players)
    p_table_players.clear()


def tournaments_report(table_obj_tournaments, tournaments):
    """ displays information of each tournament"""
    table_obj_tournaments.field_names = ["n°", "Nom", "Date", "Lieu", "Rounds joués", "controle temps",
                                         "description"]
    for i in range(len(tournaments)):
        table_obj_tournaments.add_row([i + 1,
                                       tournaments[i]['name'],
                                       tournaments[i]['date'],
                                       tournaments[i]['location'],
                                       len(tournaments[i]['rounds']),
                                       tournaments[i]['time_control'],
                                       tournaments[i]['notes']
                                       ])

    print("\n\t\tTournois sauvegardés")
    print(f"\n{table_obj_tournaments}\n")

    for i in range(len(tournaments)):
        print(f"\n\t\t   Liste des joueurs du tournoi {i + 1}:\n")
        players_to_display = tournaments[i]['players']
        players_reports(1, players_to_display)
        table_obj_tournaments.clear()


def rounds_reports(rounds_to_display):
    """Takes in input the list of rounds of the tournament chosen by the user.
    Displays information of each round of this tournament """

    p_table_round = PrettyTable()
    column_names = ["paires", " résultats", "date de début", "date de fin"]
    pairs = []
    results = []
    if len(rounds_to_display) == 0:
        print("\n\t*** CE TOURNOI NE COMPORTE AUCUN ROUND. CHOISISSEZ UN AUTRE TOURNOI ***")
    else:
        for i in range(len(rounds_to_display)):
            for j in range(4):
                player_1 = rounds_to_display[i][3][j][0]['name'] + " " + rounds_to_display[i][3][j][0]['first_name']
                player_2 = rounds_to_display[i][3][j][1]['name'] + " " + rounds_to_display[i][3][j][1]['first_name']
                pairs.extend([[player_1, player_2]])
                result_1 = rounds_to_display[i][4][j][0][1]
                result_2 = rounds_to_display[i][4][j][1][1]
                results.extend([[result_1, result_2]])

            print(f"\n\tRound {i + 1} : ")

            p_table_round.add_column(column_names[0], [pairs[0], pairs[1], pairs[2], pairs[3]])
            p_table_round.add_column(column_names[1], [results[0], results[1], results[2], results[3]])
            p_table_round.add_column(column_names[2], [rounds_to_display[i][1], "", "", ""])
            p_table_round.add_column(column_names[3], [rounds_to_display[i][2], "", "", ""])

            print(p_table_round)
            p_table_round.clear()
            pairs = []
            results = []


def no_tournaments():
    print("\n\t\t *** IL N'EXISTE AUCUN TOURNOI SAUVEGARDE ***")
    press_to_clear.enter_to_clear()
    os.system('cls')


def no_players():
    print("\n\t\t *** IL N'EXISTE AUCUN JOUEUR SAUVEGARDE ***")
    press_to_clear.enter_to_clear()
    os.system('cls')
