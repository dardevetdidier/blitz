from pprint import pprint
from os import system
from tinydb import TinyDB, Query
from tinydb.operations import set
from prettytable import PrettyTable
from views.art import enter_scores, tournament_menu_art, main_menu_art, logo, ranking_menu_art, report_menu_art,\
    player_reports_art, tournaments_reports_art
from models.tournament import Tournament
from models.rounds import Round
from models.players import Player
from controllers.launch_tournament import launch_tournament
from controllers.enter_results import enter_results
from controllers.confirm import confirm_action
from controllers.press_to_clear import enter_to_clear
from controllers.generates_players import generates_players, enters_player_info
from views.menu import display_main_menu, display_tournament_menu, display_tournament_running, display_player_menu,\
    display_ranking_menu, display_report_menu, display_players_report, display_tournaments_report, choose_item
from views.reports import t_to_load


# ***************** --> MAIN *****************************

def main():
    tournament_db = TinyDB('tournaments.json', encoding='utf-8', ensure_ascii=False, indent=4)
    players_db = TinyDB('players.json', encoding='utf-8', ensure_ascii=False, indent=4)
    query = Query()
    pairs_sort_rank = []
    player = Player(None, None, None, None, None, None, None)
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
        print(logo)
        print(main_menu_art)
        display_tournament_running(tournament.tournament_is_on, tournament.name)
        display_main_menu()

        user_choice = choose_item(5)

        # **** TOURNAMENT MENU *****************************************************************************

        if user_choice == 1:
            system('cls')

            while True:
                print(tournament_menu_art)
                display_tournament_running(tournament.tournament_is_on, tournament.name)
                display_tournament_menu()
                user_choice = choose_item(6)

                # **** NEW TOURNAMENT ****************************************************************

                if user_choice == 1:
                    if confirm_action() == 2:
                        system('cls')
                        continue
                    else:
                        system('cls')
                        if not tournament.tournament_is_on:
                            # create a tournament - user enters the information
                            players = generates_players(len(players_db), players_db)
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

                # **** LOAD TOURNAMENT ****************************************************************

                elif user_choice == 2:
                    system('cls')

                    serialized_tournaments = tournament_db.all()
                    # pprint(serialized_tournaments, sort_dicts=False)

                    # display tournaments with prettytable
                    p_table.field_names = ["n°", "nom", "date", "lieu", "rounds joués"]

                    # for i in range(len(serialized_tournaments)):
                    #     p_table.add_row([i + 1,
                    #     serialized_tournaments[i]['name'],
                    #     serialized_tournaments[i]['date'],
                    #     serialized_tournaments[i]['location'],
                    #     len(serialized_tournaments[i]['rounds'])])
                    #
                    # print("\n\t\tTournois sauvegardés")
                    # print(f"\n{p_table}")
                    #
                    # tournament_to_load = 0
                    # while True:
                    #     try:
                    #         tournament_to_load = int(input("\n\tChoisissez le n° du tournoi à charger: "))
                    #         if t_to_load in range(1, len(serialized_tournaments) + 1):
                    #             break
                    #     except ValueError:
                    #         continue

                    tournament_to_load = t_to_load(p_table, serialized_tournaments)

                    # create new tournament instance using tournament db
                    tournament = Tournament.deserialize_tournament(serialized_tournaments[tournament_to_load - 1])
                    round_number = len(tournament.rounds) + 1
                    if not round_number > tournament.num_rounds:
                        tournament.tournament_is_on = True

                    p_table.clear()
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

                            if not (round_number > tournament.num_rounds and not round_is_on):
                                start_round = rnd.starts_round(round_number, tournament.name)
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

                # ********************************* ENTER RESULTS AND FINISHES ROUND   ****************************

                elif user_choice == 4:
                    if confirm_action() == 2:
                        system('cls')
                        continue
                    else:
                        system('cls')
                        print(enter_scores)
                        if round_is_on:
                            # ********************  ENTER RESULTS  ********************************
                            results_list = []
                            print()
                            if round_number == 1:
                                for i in range(len(pairs_sort_rank)):
                                    results = enter_results(pairs_sort_rank[i][0], pairs_sort_rank[i][-1])
                                    results_list.append(results)
                            else:
                                pairs_sort_score = tournament.pairs_by_score(tournament.sort_by_score())
                                for i in range(len(pairs_sort_score)):
                                    results = enter_results(pairs_sort_score[i][0], pairs_sort_score[i][-1])
                                    results_list.append(results)

                            # ******************  FINISHES THE ROUND  *******************************

                            round_ended = rnd.ends_round(results_list)
                            round_is_on = False

                            # *******  sends round information into rounds attribut of tournament class

                            tournament.rounds.append(round_ended)

                            # *********************  UPDATE TOURNAMENT DB  *********************************

                            tournament_db.update({'rounds': tournament.rounds}, query.name == tournament.
                                                 serialize_tournament['name'])
                            tournament_db.update({'players': tournament.players}, query.name == tournament.
                                                 serialize_tournament['name'])

                            # for player in range(len(tournament.players)):
                            #     players_db.update({'total_score': tournament.serialize_tournament['players'][player]
                            #     ['total_score']})

                            # **********************  UPDATE PLAYERS_DB ************************************

                            for player in range(len(tournament.players)):
                                players_db.update(set('total_score', tournament.players[player]['total_score']),
                                                  query.player_id == tournament.players[player]['player_id'])

                            # for player in range(len(tournament.players)):
                            #     players_db.remove(query.player_id == tournament.players[player]['player_id'])
                            # players_db.insert_multiple(tournament.serialize_tournament['players'])

                            print("\n\tLes résultats du round sont bien enregistrés.")
                            print(f"\n\t     ****  LE ROUND {round_number} EST TERMINE  ****")
                            # print(f"round_number = {round_number}    num_rounds = {tournament.num_rounds}")
                            # print(tournament.tournament_is_on)
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

                # **** QUIT TOURNAMENT ****************************************************************

                elif user_choice == 5:
                    print("\n\tInterrrompre le tournoi et retourner au menu principal ?")
                    if confirm_action() == 2:
                        system('cls')
                    else:
                        if tournament.tournament_is_on:
                            tournament.tournament_is_on = False
                            round_number = 1
                            print("\n\tLe tournoi a bien été interrompu.")
                            main()
                        else:
                            print("\n\tIl n'y a pas de tournoi en cours.")
                        enter_to_clear()
                        continue

                # **** RETURN MAIN MENU ****************************************************************

                elif user_choice == 6:
                    break

        # **** PLAYER MENU *****************************************************************************

        elif user_choice == 2:
            system('cls')
            while True:
                display_player_menu()
                user_choice = choose_item(3)

                if user_choice == 1:
                    system('cls')
                    enters_player_info(players_db)

                elif user_choice == 2:
                    pass
                elif user_choice == 3:
                    break

        # **** RANKING MENU *****************************************************************************

        elif user_choice == 3:
            system('cls')
            print(ranking_menu_art)
            display_ranking_menu()
            user_choice = choose_item(3)

            if user_choice == 1:
                pass
            elif user_choice == 2:
                pass
            elif user_choice == 3:
                pass

        # **** REPORT MENU *****************************************************************************

        elif user_choice == 4:
            system('cls')
            while True:
                print(report_menu_art)
                display_report_menu()
                user_choice = choose_item(3)

                if user_choice == 1:
                    system('cls')
                    print(player_reports_art)
                    display_players_report()
                    user_choice = choose_item(3)

                    if user_choice == 1:
                        pass
                    elif user_choice == 2:
                        pass
                    elif user_choice == 3:
                        system('cls')
                        continue

                elif user_choice == 2:
                    system('cls')
                    print(tournaments_reports_art)
                    display_tournaments_report()
                elif user_choice == 3:
                    break

        # **** EXIT APP *****************************************************************************

        elif user_choice == 5:
            system('cls')
            exit()


main()

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
