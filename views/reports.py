from prettytable import PrettyTable


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
            tournament_to_load = int(input("\n  --> Choisissez le n° du tournoi : "))
            if tournament_to_load in range(1, len(tournaments) + 1):
                break
        except ValueError:
            continue

    table_obj.clear()
    return tournament_to_load


def players_reports(user_choice, table_obj, players):
    """displays a table of players sorted by name or ranking"""

    for i in range(len(players)):
        table_obj.add_row([players[i]['player_id'],
                           players[i]['name'],
                           players[i]['first_name'],
                           players[i]['birth'],
                           (players[i]['rank'])
                           ])
    if user_choice == 1:
        table_obj.sortby = "Nom"
    elif user_choice == 2:
        table_obj.sortby = "Classement"

    print(table_obj)


def tournaments_report(table_obj_tournaments, table_obj_players, tournaments):
    """ displays information of each tournament"""

    for i in range(len(tournaments)):
        table_obj_tournaments.add_row([i + 1,
                                       tournaments[i]['name'],
                                       tournaments[i]['date'],
                                       tournaments[i]['location'],
                                       len(tournaments[i]['rounds'])
                                       ])

    print("\n\t\tTournois sauvegardés")
    print(f"\n{table_obj_tournaments}\n")

    for i in range(len(tournaments)):
        table_obj_players.field_names = ["Identifiant", "Nom", "Prénom", "Date de naissance",
                                         "Classement"]
        print(f"\n\t\tListe des joueurs du tournoi {i + 1}:\n")
        players_to_display = tournaments[i - 1]['players']
        players_reports(1, table_obj_players, players_to_display)
        table_obj_players.clear()


def rounds_reports(rounds_to_display):
    """Takes in input the list of rounds of the tournament chosen by the user.
    Displays information of each round of this tournament """

    p_table_round = PrettyTable()
    # p_table_round.field_names = ["paires", "date de début", "date de fin"]
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
