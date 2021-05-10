import json


# sort list of players by rank
def sort_by_rank():
    with open("joueurs.json", "r", encoding="utf-8") as f:
        players = json.load(f)
    rank_sorted_list = sorted(players, key=lambda k: k['classement'])

    return rank_sorted_list


class Match:
    def __init__(self):
        for index in range(0, 1):
            self.player1 = sort_by_rank()[index]
            self.player2 = sort_by_rank()[index + 4]
        self.player1_score = 0
        self.player2_score = 0

    def enter_result(self):
        self.player1_score = int(input(f"Entrez le score de {self.player1['nom']} {self.player1['prenom']} : "))
        self.player2_score = int(input(f"Entrez le score de {self.player2['nom']} {self.player2['prenom']} : "))
        result = ([self.player1['nom'] + self.player1["prenom"], self.player1_score],
                  [self.player2['nom'] + self.player2["prenom"], self.player2_score])
        return result
