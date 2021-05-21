from .art import logo, main_menu_art, tournament_menu_art, player_menu_art


def choose_item(items):
    user_choice = 0
    while True:
        try:
            user_choice = int(input("    --> Entrez votre choix: "))
            if user_choice in range(1, items + 1):
                break
        except ValueError:
            continue
    return user_choice


def display_main_menu():
    print(logo)
    print(main_menu_art)
    print("""
\t|  1: Menu Tournoi
\t|  2: Menu Joueurs
\t|  3: Menu Classement
\t|  4: Menu Rapports
\t|  5: Quitter
""")


def display_tournament_menu():
    print(tournament_menu_art)
    print("""
\t|  1: Créer un tournoi
\t|  2: Charger un tournoi
\t|  3: Débuter un round
\t|  4: Entrer les résultats et terminer le round
\t|  5: Retour menu principal
""")


def display_player_menu():
    print(player_menu_art)
    print("""
\t|  1: Ajouter un joueur à la base de données
\t|  2: Voir la liste des joueurs
\t|  3: Retour menu principal
""")
