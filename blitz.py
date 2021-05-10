import json
from match import sort_by_rank, Match


class Player:

    def __init__(self):
        self.name = input("Nom : ")
        self.first_name = input("Prénom : ")
        self.birth = input("Date de naissance : ")
        self.sex = input("Sexe : ")
        self.rank = int(input("Classement : "))
        # self.score = 0
        # self.total_score = 0

        self.player = {
            'nom': self.name,
            'prenom': self.first_name,
            'date de naissance': self.birth,
            'sexe': self.sex,
            'classement': self.rank
        }

    def save_player(self):
        """load json file, add player (dict) into file return the list of all players"""
        with open("joueurs.json", "r", encoding="utf-8") as f:
            players = json.load(f)

        players.append(self.player)

        with open('joueurs.json', "w", encoding="utf-8") as f:
            json.dump(players, f, indent=4, ensure_ascii=False)

    def print_player(self):
        pass


# generates one pair
class StartingPair:
    starting_pair = []

    def __init__(self):
        for index in range(0, 1):
            self.player1 = sort_by_rank()[index]
            self.player2 = sort_by_rank()[index + 4]
            self.starting_pair.extend([self.player1, self.player2])


# generates 4 starting pairs
class StartingAllPairs:
    starting_pairs_list = []

    def __init__(self):
        for index in range(0, 4):
            self.starting_pair = []
            self.player1 = sort_by_rank()[index]
            self.player2 = sort_by_rank()[index + 4]
            self.starting_pair.extend([self.player1, self.player2])
            StartingAllPairs.starting_pairs_list.append(self.starting_pair)


class Round:
    def __init__(self):
        self.round_name = ""
        self.start_date = ""
        self.start_hour = ""
        self.end_date = ""
        self.end_hour = ""
        self.all_pairs = StartingAllPairs


class Tournament:
    def __init__(self):
        self.t_name = input("Nom du tournoi : ")
        self.t_location = input("Lieu du tournoi :  ")
        self.t_date = input("Date du tournoi : ")
        self.t_turns = 4
        self.t_rounds = StartingAllPairs
        self.t_time_control = input("'Bullet', 'Blitz' ou 'Coup rapide'? : ")
        self.t_notes = input("Remarques du directeur : ")

    def display_tournament_infos(self):
        pass


print(sort_by_rank())
match = Match()
print(match.enter_result())

# pairs = StartingPair()
# print(pairs.starting_pair)

# Créer 8 joueurs
# for i in range(1, 9):
#     print(f"\nEntrez les informations du joueur {i} :\n ")
#     player = Player()
#     player.save_player()

# ajouter joueur à la base de donnée


# TODO 2 : Créer paire de joueurs -> système suisse

# TODO 3 : Créer résultats avec (inputs) -> fichier json ?
