from prettytable import PrettyTable


def t_to_load(table_obj, tournaments):
    for i in range(len(tournaments)):
        table_obj.add_row([i + 1, tournaments[i]['name'], tournaments[i]['date'],
                           tournaments[i]['location'], len(tournaments[i]['rounds'])])

    print("\n\t\tTournois sauvegardés")
    print(f"\n{table_obj}")
    tournament_to_load = 0
    while True:
        try:
            tournament_to_load = int(input("\n\tChoisissez le n° du tournoi à charger: "))
            if tournament_to_load in range(1, len(tournaments) + 1):
                break
        except ValueError:
            continue

    return tournament_to_load
