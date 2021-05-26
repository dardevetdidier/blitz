from .art import player_menu_art


def choose_item(items):
    user_choice = 0
    while True:
        try:
            user_choice = int(input("\t     --> Entrez votre choix: "))
            if user_choice in range(1, items + 1):
                break
        except ValueError:
            continue
    return user_choice


def display_main_menu():
    print(f"""
\t\t\t|  1: Menu Tournoi
\t\t\t|  2: Menu Joueurs
\t\t\t|  3: Menu Classement
\t\t\t|  4: Menu Rapports
\t\t\t|  5: Quitter
""")


def display_tournament_menu():
    print("""
\t\t\t|  1: Créer un tournoi
\t\t\t|  2: Charger un tournoi
\t\t\t|  3: Débuter un round
\t\t\t|  4: Entrer les résultats et terminer le round
\t\t\t|  5: Interrompre le tournoi en cours
\t\t\t|  6: Retour Menu Principal
""")


def display_player_menu():
    print(player_menu_art)
    print("""
\t\t\t|  1: Ajouter un joueur à la base de données
\t\t\t|  2: Afficher la liste des joueurs
\t\t\t|  3: Retour Menu Principal
""")


def display_ranking_menu():
    print("""
\t\t\t|  1: Modifier le classement d'un joueur
\t\t\t|  2: Afficher le classement des joueurs
\t\t\t|  3: Retour Menu Principal
""")


def display_report_menu():
    print("""
\t\t\t|  1: Rapports Joueurs
\t\t\t|  2: Rapports Tournois
\t\t\t|  3: Retour Menu Principal
""")


def display_players_report():
    print("""
\t\t\t|  1: Afficher les joueurs enregistrés
\t\t\t|  2: Afficher les joueurs d'un tournoi
\t\t\t|  3: Retour Menu Rapport
""")


def display_alpha_or_rank():
    print("""
\t\t\t|  Afficher les joueurs:
\t\t\t|     1: Par ordre alphabétique
\t\t\t|     2: Par classement
\t\t\t|     3: Retour
""")


def display_tournaments_report():
    print("""
\t\t\t|  1: Afficher tous les tournois
\t\t\t|  2: Afficher les tours d'un tournoi
\t\t\t|  3: Afficher les matches d'un tournoi
\t\t\t|  4: Retour Menu Rapport
""")

def display_tournament_running(t_is_on, tournoi):
    if t_is_on:
        print(f"\n\t     *** Le tournoi '{tournoi}' est en cours d'exécution ***")
    else:
        print("\n\t     *** Il n'y a pas de tournoi en cours d'exécution. ***")
