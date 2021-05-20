from tinydb import TinyDB, Query
from models.tournament import Tournament
from controllers.launch_tournament import launch_tournament
from controllers.enter_results import enter_results
from controllers.confirm import confirm_action
from models.rounds import Round
from views.menu import display_main_menu, display_tournament_menu, choose_item

from pprint import pprint

# ***************** --> MAIN *****************************
tournament_db = TinyDB('tournaments.json', encoding='utf-8', ensure_ascii=False)
query = Query()
pairs_sort_rank = []
tournament = Tournament(None, None, None, None, None, None)
round_number = 1
rnd = Round(None)
app_is_on = True

# TODO : verifier le systeme de pairs par score
# TODO : mettre à jour le total score
# TODO : implémenter continuer tournoi -> load
while app_is_on:
    display_main_menu()
    user_choice = choose_item(5)

    if user_choice == 1:

        while True:
            display_tournament_menu()
            user_choice = choose_item(4)
            if user_choice == 1:
                if confirm_action() == 2:
                    display_tournament_menu()
                else:
                    if not tournament.tournament_is_on:
                        # create a tournament - user enters the information
                        tournament = launch_tournament()
                        tournament.insert_db(tournament_db)
                        tournament.display_tournament_infos()

                        # sys create pairs of players sorted by ranking
                        pairs_sort_rank = tournament.pairs_by_rank()
                        print("\nLes informations du tournoi ont bien été enregistrées.")
                        input("\nAppuyez sur 'Entrée' pour revenir au menu précédent: ")
                        continue
                    else:
                        print("\nUn tournoi est déjà en cours.")
                        input("Appuyez sur 'Entrée' pour revenir au menu précedent: ")
                        continue

            elif user_choice == 2:
                if confirm_action() == 2:  # User doesn't confirm -> previous menu
                    display_tournament_menu()
                else:
                    if tournament.tournament_is_on:
                        # system creates a round
                        if round_number == 1:
                            rnd = Round(pairs_sort_rank)
                        else:
                            rnd = Round(tournament.pairs_by_score())
                        # num_rounds = tournament_db.get(query['num_rounds'] > 0)
                        start_round = rnd.starts_round(round_number, tournament.num_rounds)
                        # affiche la liste des joueurs triés par score total
                        print(f"\nListe des joueurs triés par score :\n")
                        pprint(tournament.pairs_by_score(), sort_dicts=False)
                        # print(num_rounds)
                        print("\nLe round a bien été créé.")
                        continue
                    else:
                        print("Impossible de démarrer un round. Il n'y a pas de tournoi en cours.")
                        continue

            elif user_choice == 3:
                if confirm_action() == 2:
                    display_tournament_menu()
                else:
                    # entrer les résultats
                    results_list = []
                    if round_number == 1:
                        for i in range(len(pairs_sort_rank)):
                            results = enter_results(pairs_sort_rank[i][0], pairs_sort_rank[i][-1])
                            results_list.append(results)
                    else:
                        pairs_sort_score = tournament.pairs_by_score()
                        print(pairs_sort_score)
                        for i in range(len(pairs_sort_score)):
                            results = enter_results(pairs_sort_score[i][0], pairs_sort_score[i][-1])
                            results_list.append(results)

                    # Finishes the round
                    print(f"\nInfos du round:\n")
                    round_ended = rnd.ends_round(results_list)
                    pprint(round_ended, sort_dicts=False)
                    # envoie les infos du round dans l'attribut rounds de la classe tournament
                    tournament.rounds.append(round_ended)
                    # update tournament db
                    tournament_db.update({'rounds': tournament.rounds})
                    round_number += 1

                    # affiche la liste des joueurs triés par score total
                    print(f"\nListe des joueurs triés par score :\n")
                    pprint(tournament.pairs_by_score(), sort_dicts=False)
            elif user_choice == 4:
                pass

    elif user_choice == 2:
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
print(f"\nListe des joueurs triés par score :\n")
pprint(tournament.pairs_by_score(), sort_dicts=False)

print(f"\npaires triées par classement:\n")
pprint(pairs_sort_rank, sort_dicts=False)
