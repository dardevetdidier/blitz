from .art import logo, main_menu_art, tournament_menu_art


def choose_item(items):
    user_choice = 0
    while True:
        try:
            user_choice = int(input("Entrez votre choix: "))
            if user_choice in range(1, items + 1):
                break
        except ValueError:
            continue
    return user_choice


def display_main_menu():
    print(logo)
    print(main_menu_art)
    print("""1: Menu Tournoi
2: Menu Joueurs
3: Menu Classement
4: Menu Rapports
5: Quitter
""")


def display_tournament_menu():
    print(tournament_menu_art)
    print("""
1: Créer un tournoi
2: Débuter un round
3: Entrer les résultats et terminer le round
4: Retour menu principal
""")
