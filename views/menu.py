def main_menu():
    print("""
****** BLITZ ******
1: Créer un tournoi
2: Ajouter un joueur à la base de données
3: Mettre à jour le classement
4: Afficher le rapport
""")

    user_choice = 0
    while True:
        try:
            user_choice = int(input("Entrez votre choix: "))
            if user_choice in range(1, 5):
                break
        except ValueError:
            continue
    return user_choice


def tournament_menu():
    print("""
****** Menu Tournoi ******
1: Entrer les informations
2: Débuter un round
3: Terminer un round
4: Entrer un résultat
5: Retour menu principal
""")

    user_choice = 0
    while True:
        try:
            user_choice = int(input("Entrez votre choix: "))
            if user_choice in range(1, 6):
                break
        except ValueError:
            continue
    return user_choice
