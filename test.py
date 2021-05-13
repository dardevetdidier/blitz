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


def sort_by_rank():
    with open("players.json", "r", encoding="utf-8") as f:
        players = json.load(f)
    rank_sorted_list = sorted(players, key=lambda k: k['rank'])
    return rank_sorted_list


def generates_players():
    """User enters informations of 8 players. returns list of 8 players"""
    players = []
    for i in range(1, 9):
        print(f"\nEntrez les informations du joueur {i} :\n ")
        player_id = i
        name = input("Nom : ")
        first_name = input("Prénom : ")
        birth = input("Date de naissance : ")
        sex = input("Sexe : ")
        rank = int(input("Classement : "))
        player = Player(player_id, name, first_name, birth, sex, rank)
        players.append(player.player)
    with open('players.json', "w", encoding='utf-8') as f:
        json.dump(players, f, indent=4, ensure_ascii=False)

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
    tournament.display_tournament_infos()
    with open('tournament.json', "w") as f:
        json.dump(tournament.tournaments, f, indent=4, ensure_ascii=False)
    return tournament


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

    def display_tournament_infos(self):
        print(self.tournaments)


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
            'rank': self.rank
        }

    def save_player(self):
        """load json file, add player (dict) into file return the list of all players"""
        with open("players.json", "r", encoding="utf-8") as f:
            players = json.load(f)

        players.append(self.player)

        with open('players.json', "w", encoding="utf-8") as f:
            json.dump(players, f, indent=4, ensure_ascii=False)


class FirstRound:
    def __init__(self, name, start_time):
        self.round_name = name
        self.start_time = start_time
        self.end_time = None  # changes when enters results
        self.pairs = StartingAllPairs.starting_pairs_list


class StartingAllPairs:
    starting_pairs_list = []

    def __init__(self):
        for index in range(0, 4):
            self.starting_pair = []
            self.player1 = sort_by_rank()[index]
            self.player2 = sort_by_rank()[index + 4]
            self.starting_pair.extend([self.player1, self.player2])
            StartingAllPairs.starting_pairs_list.append(self.starting_pair)


# Cette classe ne sert à rien !!!! cf def enter_results
class Results:
    def __init__(self, player1_score, player2_score):
        for index in range(0, 1):
            self.player1 = sort_by_rank()[index]
            self.player2 = sort_by_rank()[index + 4]
        self.player1_score = player1_score
        self.player2_score = player2_score

    def save_results(self):
        scores = ([f"{self.player1['name']} {self.player1['first_name']}", self.player1_score],
                  [f"{self.player2['name']} {self.player2['first_name']}", self.player2_score])

        return scores


def enter_results(player1, player2):
    """User enters results of the round. Returns Tuple of 2 lists ([player1, score1], [player2, score2])"""
    player1_score = 0.0
    player2_score = 0.0
    while not player1_score + player2_score == 1:
        player1_score = float(input(f"\nEntrez le score de {player1['name']} {player1['first_name']} : "))
        player2_score = float(input(f"Entrez le score de {player2['name']} {player2['first_name']} : "))
    # TODO : Ajouter score au total score -> json ou instance ?
    result = ([f"{player1['name']} {player1['first_name']}", player1_score],
              [f"{player2['name']} {player2['first_name']}", player2_score])
    # result = Results(player1_score, player2_score).save_results()
    return result


# launch_tournament()
pairs = StartingAllPairs().starting_pairs_list
pprint.pprint(pairs, sort_dicts=False)

results_list = []
for i in range(len(pairs)):
    results = enter_results(pairs[i][0], pairs[i][-1])
    print(results)
    results_list.append(results)
pprint.pprint(results_list)
