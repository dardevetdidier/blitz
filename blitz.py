from tinydb import TinyDB, Query
from models.tournament import Tournament
from models.rounds import Round
from models.players import Player
from controllers.launch_tournament import launch_tournament
from controllers.enter_results import enter_results
from controllers.confirm import confirm_action
from controllers.press_to_clear import enter_to_clear
from controllers.generates_players import generates_players, enters_player_info
from views.menu import display_main_menu, display_tournament_menu, display_player_menu, choose_item
# from pprint import pprint
from os import system
from prettytable import PrettyTable

# ***************** --> MAIN *****************************
tournament_db = TinyDB('tournaments.json', encoding='utf-8', ensure_ascii=False, indent=4)
players_db = TinyDB('players.json', encoding='utf-8', ensure_ascii=False, indent=4)
query = Query()
pairs_sort_rank = []
player = Player(None, None, None, None, None, None)
tournament = Tournament(None, None, None, None, None, None, None)

round_is_on = False
rnd = Round(None)
round_number = len(rnd.round_list) + 1
app_is_on = True
p_table = PrettyTable()
p_table.align = "c"

# TODO : implémenter continuer tournoi -> load
while app_is_on:
    system('cls')
    display_main_menu()
    user_choice = choose_item(5)

    # **** TOURNAMENT MENU *****************************************************************************

    if user_choice == 1:
        system('cls')

        while True:
            display_tournament_menu()
            user_choice = choose_item(5)

            # **** NEW TOURNAMENT ****************************************************************

            if user_choice == 1:
                if confirm_action() == 2:
                    system('cls')
                    continue
                else:
                    system('cls')
                    if not tournament.tournament_is_on:
                        # create a tournament - user enters the information
                        players = generates_players(len(players_db))
                        tournament = launch_tournament(players)
                        tournament.insert_db(tournament_db)
                        # player.add_player_to_db(players_db)

                        # tournament.display_tournament_infos()

                        # sys create pairs of players sorted by ranking
                        pairs_sort_rank = tournament.pairs_by_rank()
                        print("\t\nLes informations du tournoi ont bien été enregistrées.")
                        input("\t\n--> Appuyez sur 'Entrée' pour continuer: ")
                        system('cls')
                        continue
                    else:
                        print("\n\tUn tournoi est déjà en cours.")
                        enter_to_clear()
                        continue

            # TODO : load tournament
            # **** LOAD TOURNAMENT ****************************************************************

            elif user_choice == 2:
                system('cls')

                serialized_tournaments = tournament_db.all()
                # pprint(serialized_tournaments, sort_dicts=False)
                p_table.field_names = ["n°", "nom", "date", "lieu"]

                for i in range(len(serialized_tournaments)):
                    p_table.add_row([i + 1, serialized_tournaments[i]['name'], serialized_tournaments[i]['date'],
                                     serialized_tournaments[i]['location']])

                print("\n\tTournois sauvegardés")
                print(f"\n{p_table}")
                t_to_load = 0
                while True:
                    try:
                        t_to_load = int(input("Choisissez le n° du tournoi à charger: "))
                        if t_to_load in range(1, len(serialized_tournaments)+1):
                            break
                    except ValueError:
                        continue

                tournament = tournament.deserialize_tournament(serialized_tournaments[t_to_load-1])
                tournament.tournament_is_on = True
                print(tournament.rounds)
                round_number = len(tournament.rounds) + 1

                enter_to_clear()
                continue

            # **** NEW ROUND ****************************************************************

            elif user_choice == 3:
                if confirm_action() == 2:  # User doesn't confirm -> previous menu
                    system('cls')
                    continue
                else:

                    if tournament.tournament_is_on:
                        # system creates a round
                        if round_number == 1:
                            rnd = Round(pairs_sort_rank)
                        else:
                            rnd = Round(tournament.pairs_by_score(tournament.sort_by_score()))
                            # affiche la liste des joueurs triés par score total
                            # print(f"\nListe des joueurs triés par score :\n")
                            # pprint(tournament.pairs_by_score(tournament.sort_by_score()), sort_dicts=False)

                        if not round_number > tournament.num_rounds and not round_is_on:
                            start_round = rnd.starts_round(round_number)
                            round_is_on = True
                            enter_to_clear()
                            continue
                        else:
                            system('cls')
                            print("\n\tUn round est déjà en cours. Entrez les résultats\n\t     avant"
                                  " la création d'un nouveau round.")
                            enter_to_clear()
                            continue
                    else:
                        print("\n\tImpossible de démarrer un round. Il n'y a pas de tournoi en cours.")
                        enter_to_clear()
                        continue

            # **** ENTER RESULTS ****************************************************************

            elif user_choice == 4:
                if confirm_action() == 2:
                    system('cls')
                    continue
                else:
                    system('cls')
                    if round_is_on:
                        # entrer les résultats
                        results_list = []
                        if round_number == 1:
                            for i in range(len(pairs_sort_rank)):
                                results = enter_results(pairs_sort_rank[i][0], pairs_sort_rank[i][-1])
                                results_list.append(results)
                        else:
                            pairs_sort_score = tournament.pairs_by_score(tournament.sort_by_score())
                            print(f"paires triées par score : {pairs_sort_score}")
                            for i in range(len(pairs_sort_score)):
                                results = enter_results(pairs_sort_score[i][0], pairs_sort_score[i][-1])
                                results_list.append(results)

                        # Finishes the round
                        # print(f"\nInfos du round:\n")
                        round_ended = rnd.ends_round(results_list)
                        round_is_on = False
                        # pprint(round_ended, sort_dicts=False)

                        # envoie les infos du round dans l'attribut rounds de la classe tournament
                        tournament.rounds.append(round_ended)

                        # update tournament db
                        tournament_db.update({'rounds': tournament.rounds})

                        print("\n\tLes résultats du round sont bien enregistrés.")
                        print(f"\n\tLe round {round_number} est terminé.")

                        if round_number == tournament.num_rounds:
                            tournament.tournament_is_on = False
                            print(f"\n\tLe tournoi '{tournament.name}' est terminé.")
                            enter_to_clear()
                        else:
                            print("\n\tVous pouvez créer un nouveau round dans le menu 'Tournoi'.")
                            enter_to_clear()
                        round_number += 1
                    else:
                        print("\n\tImpossible de rentrer les résultats. Aucun round n'est en cours.")
                        enter_to_clear()
                        continue

                    # affiche la liste des joueurs triés par score total
                    # print(f"\nListe des joueurs triés par score :\n")
                    # pprint(tournament.pairs_by_score(tournament.sort_by_score()), sort_dicts=False)

            # **** RETURN MAIN MENU ****************************************************************

            elif user_choice == 5:
                break

    # **** PLAYER MENU *****************************************************************************
    elif user_choice == 2:
        system('cls')
        while True:
            display_player_menu()
            user_choice = choose_item(3)

            if user_choice == 1:
                system('cls')
                enters_player_info()

            if user_choice == 2:
                pass
            if user_choice == 3:
                break

    elif user_choice == 3:
        pass
    elif user_choice == 4:
        pass
    elif user_choice == 5:
        exit()


# affiche la liste des resultats par pairs
# print(f"Resultats par pairs:\n")
# pprint(results_list)

# envoie les infos du round dans l'attribut rounds de la classe tournament
# tournament.rounds.append(round_ended)
# tournament_1.serialized_tournament['rounds'].append(round_ended)

# affiche les infos du tournoi
# print(f"\ninfos du tournoi:\n")
# pprint(tournament.display_tournament_infos(), sort_dicts=False)

# affiche la liste des joueurs triés par score total
# print(f"\nListe des paires triés par score :\n")
# pprint(tournament.pairs_by_score(), sort_dicts=False)
#
# print(f"\npaires triées par classement:\n")
# pprint(pairs_sort_rank, sort_dicts=False)
