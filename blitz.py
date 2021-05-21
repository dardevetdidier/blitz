from tinydb import TinyDB, Query
from models.tournament import Tournament
from controllers.launch_tournament import launch_tournament
from controllers.enter_results import enter_results
from controllers.confirm import confirm_action
from controllers.press_to_clear import enter_to_clear
from models.rounds import Round
from views.menu import display_main_menu, display_tournament_menu, display_player_menu, choose_item

from pprint import pprint
from os import system

# ***************** --> MAIN *****************************
tournament_db = TinyDB('tournaments.json', encoding='utf-8', ensure_ascii=False)
players_db = TinyDB('players.json', encoding='utf-8', ensure_ascii=False)
query = Query()
pairs_sort_rank = []
tournament = Tournament(None, None, None, None, None, None)
round_number = 1
rnd = Round(None)
app_is_on = True

# TODO : implémenter continuer tournoi -> load
while app_is_on:
    system('cls')
    display_main_menu()
    user_choice = choose_item(5)

    if user_choice == 1:
        system('cls')

        while True:
            display_tournament_menu()
            user_choice = choose_item(5)

            if user_choice == 1:
                if confirm_action() == 2:
                    system('cls')
                    continue
                else:
                    system('cls')
                    if not tournament.tournament_is_on:
                        # create a tournament - user enters the information
                        tournament = launch_tournament()
                        tournament.insert_db(tournament_db)
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

            elif user_choice == 2:
                print("\n\tChoisissez un tournoi à charger:")
                pprint(tournament_db.search(query.name.exists()), sort_dicts=False)

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

                        start_round = rnd.starts_round(round_number, tournament.num_rounds)

                        print(f"\n\tLe round {round_number} a bien été créé.")
                        enter_to_clear()
                        continue

                    else:
                        print("\n\tImpossible de démarrer un round. Il n'y a pas de tournoi en cours.")
                        enter_to_clear()
                        continue

            elif user_choice == 4:
                if confirm_action() == 2:
                    system('cls')
                    continue
                else:
                    system('cls')
                    if rnd.round_is_on:
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
                        # pprint(round_ended, sort_dicts=False)

                        # envoie les infos du round dans l'attribut rounds de la classe tournament
                        tournament.rounds.append(round_ended)

                        # update tournament db
                        tournament_db.update({'rounds': tournament.rounds})
                        round_number += 1
                        print("\n\tLes résultats sont bien enregistrés.")
                        print(f"\n\tLe round {round_number} est terminé.")

                        if round_number == tournament.num_rounds:
                            tournament.tournament_is_on = False
                            print(f"\n\tLe tournoi '{tournament.name}' est terminé.")
                            enter_to_clear()
                        else:
                            print("\n\tVous pouvez créer un nouveau round dans le menu 'Tournoi'.")
                            enter_to_clear()
                    else:
                        print("\n\tImpossible de rentrer les résultats. Aucun round n'est en cours.")
                        enter_to_clear()
                        continue

                    # affiche la liste des joueurs triés par score total
                    # print(f"\nListe des joueurs triés par score :\n")
                    # pprint(tournament.pairs_by_score(tournament.sort_by_score()), sort_dicts=False)
            elif user_choice == 5:
                break

    elif user_choice == 2:
        system('cls')
        while True:
            display_player_menu()
            user_choice = choose_item(3)

            if user_choice == 1:
                pass
            if user_choice == 2:
                pass
            if user_choice == 3:
                break


        pass
    elif user_choice == 3:
        pass
    elif user_choice == 4:
        pass
    elif user_choice == 5:
        pass


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
