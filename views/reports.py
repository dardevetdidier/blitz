from prettytable import PrettyTable


def display_tournaments_table(tournaments):
    """
    displays a table of all tournaments with various information
    """
    table_tournament = PrettyTable()
    table_tournament.field_names = ["n°", "Nom", "Date", "Lieu", "Rounds joués", "controle temps",
                                    "description"]
    for i in range(len(tournaments)):
        table_tournament.add_row([i + 1,
                                  tournaments[i]['name'],
                                  tournaments[i]['date'],
                                  tournaments[i]['location'],
                                  len(tournaments[i]['rounds']),
                                  tournaments[i]['time_control'],
                                  tournaments[i]['notes']
                                  ])

    print("\n\t\t\t\tTournois sauvegardés")
    print(f"\n{table_tournament}\n")
    table_tournament.clear()


def t_to_load(tournaments):
    """
    prints a table of all tournaments. User choose a tournament. Returns the number of the tournament (int)
    """
    display_tournaments_table(tournaments)
    tournament_to_load = 0
    while True:
        try:
            tournament_to_load = int(input("\n    --> Choisissez le n° du tournoi : "))
            if tournament_to_load in range(1, len(tournaments) + 1):
                break
        except ValueError:
            continue

    return tournament_to_load


def tournaments_report(table_obj_tournaments, tournaments):
    """
    displays information of each tournament
    """
    display_tournaments_table(tournaments)

    for i in range(len(tournaments)):
        print(f"\n\t\t   Liste des joueurs du tournoi {i + 1}:")
        players_to_display = tournaments[i]['players']
        players_reports(1, players_to_display)
        table_obj_tournaments.clear()


def rounds_reports(tournaments):
    """
    Takes in input all the tournaments in db. User choose a tournament.
    Displays information of each round of this tournament.
    """
    tournament_to_load = t_to_load(tournaments)
    rounds_to_display = tournaments[tournament_to_load - 1]['rounds']
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


def players_reports(user_choice, players):
    """
    Displays a table of players sorted by name or ranking according to user choice.
    """
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

    print(f"\n{p_table_players}")
    p_table_players.clear()
