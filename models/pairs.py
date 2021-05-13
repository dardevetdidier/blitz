# from controllers.generates_players import generates_players


# sort list of players by rank
def sort_by_rank():
    # with open("players.json", "r", encoding="utf-8") as f:
    #     players = json.load(f)
    rank_sorted_list = sorted(generates_players(), key=lambda k: k['classement'])
    return rank_sorted_list


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

