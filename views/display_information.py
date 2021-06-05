import os

from controllers import press_to_clear
from controllers.press_to_clear import enter_to_clear


def display_info_end_round(round_nb, tournament):
    """
    displays information when a round is over.
    """
    if round_nb == tournament.num_rounds:
        tournament.tournament_is_on = False
        print(f"\n\tLe tournoi '{tournament.name}' est terminé.")
        enter_to_clear()
    else:
        print("\n\tVous pouvez créer un nouveau round dans le menu 'Tournoi'.")
        enter_to_clear()
    round_nb += 1


def display_info_exit_tournament(tournament):
    """
    displays information when the user leaves tournament
    """
    if tournament.tournament_is_on:
        tournament.tournament_is_on = False
        print("\n\tLe tournoi a bien été interrompu.")
        enter_to_clear()
    else:
        print("\n\tIl n'y a pas de tournoi en cours.")
        enter_to_clear()


def display_info_tournament_already_running():
    """
    displays information if a tournament is already running
    """
    print("\n\t*** Un tournoi est déjà en cours. ***")
    enter_to_clear()


def no_tournaments():
    """
    displays information if there's not tournament saved in database
    """
    print("\n\t\t *** IL N'EXISTE AUCUN TOURNOI SAUVEGARDE ***")
    press_to_clear.enter_to_clear()
    os.system('cls')


def no_players():
    """
    displays information if there's not players saved in database
    """
    print("\n\t\t *** IL N'EXISTE AUCUN JOUEUR SAUVEGARDE ***")
    press_to_clear.enter_to_clear()
    os.system('cls')
