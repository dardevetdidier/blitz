import json

class Joueur:

    def __init__(self):
        self.nom = input("Nom : ")
        self.prenom = input("Prénom : ")
        self.date_naissance = input("Date de naissance : ")
        self.sexe = input("Sexe : ")
        self.classement = input("Classement : ")

    def ajouter_joueur(self):
        with open("joueurs.json", "r", encoding="utf-8") as f:
            joueurs = json.load(f)
        joueur = {
            'nom': self.nom,
            'prenom': self.prenom,
            'date de naissance': self.date_naissance,
            'sexe': self.sexe,
            'classement': self.classement
        }
        joueurs.append(joueur)

        with open('joueurs.json', "w", encoding="utf-8") as f:
            json.dump(joueurs, f, indent=4, ensure_ascii=False)


joueur1 = Joueur()
joueur1.ajouter_joueur()

# TODO 2 : Créer paire de joueurs -> système suisse

# TODO 3 : Créer résultats avec (inputs) -> fichier json ?
