# joueurs = [{
#         "nom": "Durant",
#         "prenom": "Paul",
#         "date de naissance": "01/01/2000",
#         "sexe": "M",
#         "classement": 76
#     },
#     {
#         "nom": "Dupont",
#         "prenom": "Coralie",
#         "date de naissance": "12/12/1994",
#         "sexe": "F",
#         "classement": 54
#     },
#     {
#         "nom": "Martin",
#         "prenom": "Elise",
#         "date de naissance": "06/06/1998",
#         "sexe": "F",
#         "classement": 49
#     },
#     {
#         "nom": "Einstein",
#         "prenom": "Albert",
#         "date de naissance": "17/02/1974",
#         "sexe": "M",
#         "classement": 2
#     },
#     {
#         "nom": "Gahan",
#         "prenom": "Dave",
#         "date de naissance": "07/03/1960",
#         "sexe": "M",
#         "classement": 6
#     },
#     {
#         "nom": "Hendrix",
#         "prenom": "Jimmy",
#         "date de naissance": "02/08/1970",
#         "sexe": "m",
#         "classement": 45
#     },
#     {
#         "nom": "Karenine",
#         "prenom": "Anna",
#         "date de naissance": "31/08/1964",
#         "sexe": "F",
#         "classement": 34
#     },
#     {
#         "nom": "Picasso",
#         "prenom": "Pablo",
#         "date de naissance": "05/09/1958",
#         "sexe": "M",
#         "classement": 18
#     }
# ]

# sort list of players by rank
import json
import pprint
from random import randint
from time import localtime, strftime

# def sort_by_rank():
#     """Sorts list of players by rank and returns a new list of players"""
#     # with open("players.json", "r", encoding="utf-8") as f:
#     #     players = json.load(f)
#     rank_sorted_list = sorted(generates_players(), key=lambda k: k['rank'])
#     return rank_sorted_list


def generates_players():
    """User enters informations of 8 players. returns list of 8 players"""
    players = []
    for player in range(1, 9):
        print(f"\nEntrez les informations du joueur {player} :\n ")
        player_id = player
        name = f"joueur "  # input("Nom : ")
        first_name = str(player)  # input("Prénom : ")
        birth = "01/01/2000"  # input("Date de naissance : ")
        sex = "m"  # input("Sexe : ")
        rank = randint(1, 50)  # int(input("Classement : "))

        player = Player(player_id, name, first_name, birth, sex, rank)
        players.append(player.player)
    # with open('players.json', "w", encoding='utf-8') as f:
    #     json.dump(players, f, indent=4, ensure_ascii=False)

    return players


def launch_tournament():
    """User enters informations of tournament and instances players"""
    name = input("Nom du tournoi : ")
    location = input("Lieu du tournoi :  ")
    date = input("Date du tournoi : ")
    time_control = input("'Bullet', 'Blitz' ou 'Coup rapide'? : ")
    notes = input("Remarques du directeur : ")

    players = generates_players()
    tournament = Tournament(name, location, date, players, time_control, notes)
    # tournament.pairs_by_rank()
    # pprint.pprint(tournament.pairs_by_rank())
    # tournament.display_tournament_infos()
    # with open('tournament.json', "w") as f:
    #     json.dump(tournament.tournaments, f, indent=4, ensure_ascii=False)
    return tournament


# --> controllers
def enter_results(player1, player2):
    """User enters results of the round. Returns Tuple of 2 lists ([player1, score1], [player2, score2])"""
    player1_score = 0.0
    player2_score = 0.0
    while not player1_score + player2_score == 1:
        player1_score = float(input(f"\nEntrez le score de {player1['name']} {player1['first_name']} : "))
        player2_score = float(input(f"Entrez le score de {player2['name']} {player2['first_name']} : "))
    # TODO : Ajouter score au total score -> json ou instance ?
    player1['total_score'] = player1_score
    player2['total_score'] = player2_score
    result = ([f"{player1['name']} {player1['first_name']}", player1_score],
              [f"{player2['name']} {player2['first_name']}", player2_score])
    # result = Results(player1_score, player2_score).save_results()
    return result


class Tournament:
    def __init__(self, name, location, date, players, time_control, notes):
        self.name = name
        self.location = location
        self.date = date
        self.players = players
        self.rounds = []
        self.num_rounds = 4
        self.time_control = time_control
        self.notes = notes

        self.tournaments = {
            'name': self.name,
            'location': self.location,
            'date': self.date,
            'players': self.players,
            'rounds': self.rounds,
            'time_control': self.time_control,
            'notes': self.notes
        }

    def pairs_by_rank(self):
        """Sorts list of players by rank and creates 4 pairs. returns a list of 4 lists of 2 players"""
        rank_sorted_list = sorted(self.players, key=lambda k: k['rank'])
        pairs_sort_by_rank = []
        for index in range(0, 4):
            pair_sort_by_rank = []
            player1 = rank_sorted_list[index]
            player2 = rank_sorted_list[index + 4]
            pair_sort_by_rank.extend([player1, player2])
            pairs_sort_by_rank.append(pair_sort_by_rank)
        return pairs_sort_by_rank

    def display_tournament_infos(self):  # -> Vue
        print(self.tournaments)

    def save_tournament(self):
        pass


class Player:

    def __init__(self, player_id, name, first_name, birth, sex, rank, ):
        self.player_id = player_id
        self.name = name
        self.first_name = first_name
        self.birth = birth
        self.sex = sex
        self.rank = rank
        self.total_score = 0

        self.player = {
            'player_id': self.player_id,
            'name': self.name,
            'first_name': self.first_name,
            'birth': self.birth,
            'sex': self.sex,
            'rank': self.rank,
            'total_score': self.total_score
        }

    def add_player_to_db(self):
        pass

    def save_player(self):
        """load json file, add player (dict) into file return the list of all players"""
        with open("players.json", "r", encoding="utf-8") as f:
            players = json.load(f)

        players.append(self.player)

        with open('players.json', "w", encoding="utf-8") as f:
            json.dump(players, f, indent=4, ensure_ascii=False)


class Round:

    def __init__(self, players_pairs):
        self.name = ''
        self.start_time = None  # changes when round is created
        self.end_time = None  # changes when round is over
        self.players_pairs = players_pairs
        self.scores = None
        self.round_is_on = False
        self.round_is_over = True
        self.round_number = 1
        self.round_list = []

    def starts_round(self, num_round):

        if not (self.round_number == num_round and self.round_is_on):
            self.round_is_on = True
            print(f"Création du round{self.round_number}\n")
            self.name = f"round_{self.round_number}"
            self.start_time = f"Début : {strftime('%a %d %b %Y %H:%M:%S', localtime())}"
            self.round_list.extend([self.name, self.start_time, self.end_time, self.players_pairs, self.scores])
        else:
            print("Création d'un round impossible")

        return self.round_list

    def ends_round(self, scores):
        if self.round_is_over:  # round_is_over is true when user chooses 'stop round' in round menu
            self.end_time = f"Fin : {strftime('%a %d %b %Y %H:%M:%S', localtime())}"
            self.round_list[2] = self.end_time
            self.round_list[-1] = scores
            self.round_number += 1
            self.round_is_on = False
        return self.round_list

    def display_round_infos(self):
        pass

# class FirstRound:
#     def __init__(self, name, start_time):
#         self.round_name = name
#         self.start_time = start_time
#         self.end_time = None  # changes when enters results
#         self.pairs = StartingAllPairs.starting_pairs_list

#
# class StartingAllPairs:  # Methode round ou tournoi ou mettre round dans tournoi
#     starting_pairs_list = []
#
#     def __init__(self):
#         for index in range(0, 4):
#             self.starting_pair = []
#             self.player1 = sort_by_rank()[index]
#             self.player2 = sort_by_rank()[index + 4]
#             self.starting_pair.extend([self.player1, self.player2])
#             StartingAllPairs.starting_pairs_list.append(self.starting_pair)


# Cette classe ne sert à rien !!!! cf def enter_results()
# class Results:
#     def __init__(self, player1_score, player2_score):
#         for index in range(0, 1):
#             self.player1 = sort_by_rank()[index]
#             self.player2 = sort_by_rank()[index + 4]
#         self.player1_score = player1_score
#         self.player2_score = player2_score
#
#     def save_results(self):
#         scores = ([f"{self.player1['name']} {self.player1['first_name']}", self.player1_score],
#                   [f"{self.player2['name']} {self.player2['first_name']}", self.player2_score])
#
#         return scores_
# créer un tournoi
pairs = launch_tournament()  # ---> objet tournament
pairs.display_tournament_infos()

# crée les paires selon le classement
pairs_sort_rank = pairs.pairs_by_rank()
pprint.pprint(pairs_sort_rank, sort_dicts=False)

# crée le premier tour
round_1 = Round(pairs_sort_rank)
print(round_1.starts_round(pairs.num_rounds))

# entrer les résultats

results_list = []
for i in range(len(pairs_sort_rank)):
    results = enter_results(pairs_sort_rank[i][0], pairs_sort_rank[i][-1])
    print(results)
    results_list.append(results)

pprint.pprint(round_1.ends_round(results_list), sort_dicts=False)

pprint.pprint(results_list)
pairs.display_tournament_infos()
