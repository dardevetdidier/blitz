def main_menu():
    print("""
****** BLITZ ******
1: Créer un tournoi
2: Ajouter un joueur à la base de données
3: Mettre à jour le classement
4: Afficher le rapport
""")

    choix = 0
    while True:
        try:
            choix = int(input("Entrez votre choix: "))
            if choix in range(1, 5):
                break
        except ValueError:
            continue
    return choix


def tournament_menu():
    print("""
****** Menu Tournoi ******
1: Entrer les informations
2: Ajouter les 8 joueurs
3: Générer une ronde
4: Entrer un résultat
""")

    choix = 0
    while True:
        try:
            choix = int(input("Entrez votre choix: "))
            if choix in range(1, 4):
                break
        except ValueError:
            continue
    return choix
