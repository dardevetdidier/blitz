from controllers.press_to_clear import enter_to_clear


def display_info_end_round(round_nb, tournament):
    if round_nb == tournament.num_rounds:
        tournament.tournament_is_on = False
        print(f"\n\tLe tournoi '{tournament.name}' est terminé.")
        enter_to_clear()
    else:
        print("\n\tVous pouvez créer un nouveau round dans le menu 'Tournoi'.")
        enter_to_clear()
    round_nb += 1


def display_info_exit_tournament(tournament):
    if tournament.tournament_is_on:
        tournament.tournament_is_on = False
        print("\n\tLe tournoi a bien été interrompu.")
        enter_to_clear()
    else:
        print("\n\tIl n'y a pas de tournoi en cours.")
        enter_to_clear()


def display_info_tournament_already_running():
    print("\n\t*** Un tournoi est déjà en cours. ***")
    enter_to_clear()
