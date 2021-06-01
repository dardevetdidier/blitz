import os
from tinydb import TinyDB, Query
from prettytable import PrettyTable
from views.art import enter_scores, tournament_menu_art, main_menu_art, logo, ranking_menu_art, report_menu_art, \
    player_reports_art, tournaments_reports_art, display_players_art, display_rounds_art, load_tournament_art
from models.tournament import Tournament
from models.rounds import Round
from controllers.launch_tournament import launch_tournament
from controllers.enter_results import creates_results_list
from controllers.confirm import confirm_action
from controllers.press_to_clear import enter_to_clear
from controllers.generates_players import generates_players, enters_player_info
from controllers.modify_rank import modify_rank
from views.menu import display_main_menu, display_tournament_menu, display_tournament_running, display_player_menu, \
    display_ranking_menu, display_report_menu, display_players_report, display_tournaments_report_menu, \
    display_alpha_or_rank, choose_item
from views.reports import t_to_load, players_reports, tournaments_report, rounds_reports
from views.display_information import display_info_end_round, display_info_exit_tournament, \
    display_info_tournament_already_running, no_tournaments, no_players


# ***************** --> MAIN *****************************

def main():
    tournament_db = TinyDB('tournaments.json', encoding='utf-8', ensure_ascii=False, indent=4)
    players_db = TinyDB('players.json', encoding='utf-8', ensure_ascii=False, indent=4)
    query = Query()
    pairs_sort_rank = []
    tournament = Tournament(None, None, None, None, None, None, None)
    round_is_on = False
    rnd = Round(None)
    round_number = len(rnd.round_list) + 1
    app_is_on = True

    p_table_tournament = PrettyTable()
    p_table_tournament.align = "c"
    p_table_players = PrettyTable()
    p_table_players.align = "c"

    while app_is_on:
        os.system('cls')
        print(logo)
        print(main_menu_art)
        display_tournament_running(tournament.tournament_is_on, tournament.name)
        display_main_menu()

        user_choice = choose_item(5)

        # **** TOURNAMENT MENU *****************************************************************************

        if user_choice == 1:
            os.system('cls')

            while True:
                print(tournament_menu_art)
                display_tournament_running(tournament.tournament_is_on, tournament.name)
                display_tournament_menu()
                user_choice = choose_item(6)

                # **** NEW TOURNAMENT ****************************************************************

                if user_choice == 1:
                    if confirm_action() == 2:
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        if not tournament.tournament_is_on:
                            # user enters the information of the players and system creates a tournament
                            players = generates_players(len(players_db))
                            tournament = launch_tournament(players)

                            # the tournament is written in DB
                            tournament.insert_db()

                            os.system('cls')
                            continue
                        else:
                            display_info_tournament_already_running()
                            continue

                # **** LOAD TOURNAMENT ****************************************************************

                elif user_choice == 2:
                    serialized_tournaments = tournament_db.all()
                    os.system('cls')
                    print(load_tournament_art)
                    # p_table_tournament.field_names = ["N°", "Nom", "Date", "Lieu", "Rounds joués"]
                    tournament_to_load = t_to_load(serialized_tournaments)

                    # create new tournament instance using tournament db
                    tournament = Tournament.deserialize_tournament(serialized_tournaments[tournament_to_load - 1])
                    round_number = len(tournament.rounds) + 1

                    tournament.switch_tournament_on(round_number)
                    # if not round_number > tournament.num_rounds:
                    #     tournament.tournament_is_on = True

                    print(f"\n\t*** Le tournoi '{serialized_tournaments[tournament_to_load - 1]['name']}'"
                          f" a bien été chargé ***")

                    enter_to_clear()
                    # p_table_tournament.clear()
                    continue

                # **** NEW ROUND ****************************************************************

                elif user_choice == 3:
                    pairs_sort_rank = tournament.pairs_by_rank()
                    if confirm_action() == 2:  # User doesn't confirm -> previous menu
                        os.system('cls')
                        continue
                    else:

                        if tournament.tournament_is_on:
                            # system creates a round - first evaluates if this is the first round or not.
                            if round_number == 1:
                                rnd = Round(pairs_sort_rank)
                            else:
                                rnd = Round(tournament.pairs_by_score(tournament.sort_by_score()))

                            # creates new round if rounds are not equals to total numbers of round and if there's no
                            # round in progress
                            if not (round_number > tournament.num_rounds and not round_is_on):
                                rnd.starts_round(round_number, tournament.name)
                                round_is_on = True
                                enter_to_clear()
                                continue
                            else:
                                os.system('cls')
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
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print(enter_scores)
                        if round_is_on:
                            # ********************  ENTER RESULTS  ********************************

                            pairs_sort_score = tournament.pairs_by_score(tournament.sort_by_score())
                            print()
                            results_list = creates_results_list(round_number, pairs_sort_rank, pairs_sort_score)

                            # ******************  FINISHES THE ROUND  *******************************

                            round_ended = rnd.ends_round(results_list)
                            round_is_on = False

                            # *******  sends round information into rounds attribut of tournament class

                            tournament.rounds.append(round_ended)

                            # *********************  UPDATE TOURNAMENT DB  *********************************

                            tournament.update_tournament_db(tournament.serialize_tournament)

                            # **********************  UPDATE PLAYERS_DB ************************************

                            tournament.update_players_score()

                            print("\n\tLes résultats du round sont bien enregistrés.")
                            print(f"\n\t     ****  LE ROUND {round_number} EST TERMINE  ****")

                            display_info_end_round(round_number, tournament)

                        else:
                            print("\n\tImpossible de rentrer les résultats. Aucun round n'est en cours.")
                            enter_to_clear()
                            continue

                # **** QUIT TOURNAMENT ****************************************************************

                elif user_choice == 5:
                    print("\n\tInterrompre le tournoi et retourner au menu principal ?")
                    if confirm_action() == 2:
                        os.system('cls')
                    else:
                        display_info_exit_tournament(tournament)
                        main()

                # **** RETURN MAIN MENU ****************************************************************

                elif user_choice == 6:
                    break

        # **** PLAYER MENU *****************************************************************************

        elif user_choice == 2:
            os.system('cls')
            while True:
                serialized_players = players_db.all()
                display_player_menu()
                user_choice = choose_item(3)

                # ******** PLAYER MENU ********* ENTER A PLAYER IN DB ***************************
                if user_choice == 1:
                    os.system('cls')
                    enters_player_info(players_db)
                    enter_to_clear()

                # ******** PLAYER MENU ********* DISPLAY ALL PLAYERS IN DB **********************

                elif user_choice == 2:
                    os.system('cls')
                    print(display_players_art)

                    # if no players in db
                    if not serialized_players:
                        no_players()
                        enter_to_clear()
                        continue
                    else:
                        display_alpha_or_rank()
                        user_choice_2 = choose_item(3)

                        if user_choice_2 == 1 or user_choice_2 == 2:
                            os.system('cls')
                            print(display_players_art)
                            print("\n\t\t    Liste des joueurs enregistrés\n")

                            players_reports(user_choice_2, serialized_players)
                            enter_to_clear()

                        else:
                            break

                # ******** PLAYER MENU ********* BACK MAIN MENU ***************************
                elif user_choice == 3:
                    break

        # **** RANKING MENU *****************************************************************************

        elif user_choice == 3:
            while True:
                os.system('cls')
                print(ranking_menu_art)
                display_ranking_menu()
                serialized_players = players_db.all()
                user_choice = choose_item(3)

                # ***** RANKING  ******************* MODIFY PLAYER'S RANKING ******************************

                if user_choice == 1:
                    os.system('cls')
                    players_reports(1, serialized_players)
                    modify_rank(players_db, query, serialized_players)

                    enter_to_clear()
                    continue

                # ***** RANKING  ******************* DISPLAY PLAYERS' RANKING ******************************

                elif user_choice == 2:
                    os.system('cls')
                    print(display_players_art)
                    players_reports(2, serialized_players)

                    enter_to_clear()
                    continue

                elif user_choice == 3:
                    break

        # **** REPORT MENU *****************************************************************************

        elif user_choice == 4:
            os.system('cls')
            while True:
                serialized_players = players_db.all()
                print(report_menu_art)
                display_report_menu()
                user_choice = choose_item(3)

                # ******** REPORTS **************  DISPLAY PLAYERS MENU ********************************

                if user_choice == 1:
                    while True:
                        os.system('cls')
                        print(player_reports_art)
                        display_players_report()
                        serialized_tournaments = tournament_db.all()
                        user_choice = choose_item(3)

                        # ****** REPORTS *****  ALL SAVED PLAYERS MENU  ************************************

                        if user_choice == 1:
                            os.system('cls')
                            print(display_players_art)
                            display_alpha_or_rank()
                            user_choice_2 = choose_item(3)

                            # user has to choose beetween display alpha or rank sort

                            if user_choice_2 == 1 or user_choice_2 == 2:
                                os.system('cls')
                                print(display_players_art)

                                players_reports(user_choice_2, serialized_players)
                                enter_to_clear()

                            elif user_choice_2 == 3:
                                continue

                        # ********* REPORTS ********  DISPLAY THE PLAYERS OF A TOURNAMENT MENU  ***********************

                        elif user_choice == 2:
                            os.system('cls')
                            print(display_players_art)
                            if not serialized_tournaments:
                                no_tournaments()
                                continue
                            else:
                                # user choose tournament to load
                                tournament_to_load = t_to_load(serialized_tournaments)
                                players_to_display = serialized_tournaments[tournament_to_load - 1]['players']

                                display_alpha_or_rank()
                                user_choice_2 = choose_item(3)

                                if user_choice_2 == 1 or user_choice_2 == 2:
                                    os.system('cls')
                                    print(display_players_art)

                                    players_reports(user_choice_2, players_to_display)

                                    enter_to_clear()
                                    p_table_tournament.clear()

                                elif user_choice_2 == 3:
                                    break

                        # ********** REPORTS ******  back to previous menu   ***********************************

                        elif user_choice == 3:
                            os.system('cls')
                            break

                # ************** REPORTS ********  DISPLAY TOURNAMENTS MENU  ******************************

                elif user_choice == 2:
                    os.system('cls')
                    while True:
                        serialized_tournaments = tournament_db.all()

                        print(tournaments_reports_art)
                        display_tournaments_report_menu()
                        user_choice = choose_item(3)

                        if user_choice == 1:
                            os.system('cls')
                            print(tournaments_reports_art)
                            if not serialized_tournaments:
                                no_tournaments()
                                break
                            else:
                                tournaments_report(p_table_tournament, serialized_tournaments)
                                enter_to_clear()
                                continue

                        # **** REPORTS *********  DISPLAY ROUNDS BY TOURNAMENT ************************

                        elif user_choice == 2:
                            os.system('cls')
                            print(display_rounds_art)
                            if not serialized_tournaments:
                                no_tournaments()
                                break
                            else:
                                # user choose tournament to load
                                # tournament_to_load = t_to_load(serialized_tournaments)
                                # rounds_to_display = serialized_tournaments[tournament_to_load - 1]['rounds']

                                # displays rounds and matches of a tournament
                                rounds_reports(serialized_tournaments)

                                enter_to_clear()
                                continue

                        # ******* REPORTS ******************  BACK TO PREVIOUS MENU  *********************

                        elif user_choice == 3:
                            os.system('cls')
                            break

                elif user_choice == 3:
                    break

        # **** EXIT APP *****************************************************************************

        elif user_choice == 5:
            print("\n\t\tQuitter le programme ?")
            if confirm_action() == 2:
                continue
            else:
                os.system('cls')
                exit()


main()
