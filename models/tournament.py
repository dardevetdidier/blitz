from pprint import pprint


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

    def pairs_by_score(self):
        """Sorts list of players by score and creates 4 pairs. If scores are equals, sort by rank.
         returns a list of 4 lists of 2 players"""

        score_sorted_list = sorted(self.players, key=lambda k: k['total_score'], reverse=True)
        # TODO : reorganiser selon MVC
        # TODO : si scores sont egaux trier en fonction du rang
        pprint(score_sorted_list)
        pairs_sort_by_score = []
        for player in range(0, 8, 2):
            pair_sort_by_score = []
            player1 = score_sorted_list[player]
            player2 = {}
            for r in range(len(self.rounds)):
                for p in range(len(self.rounds[r][4])):

                    if not (score_sorted_list[player]['player_id'] in self.rounds[r][4][p] and
                            score_sorted_list[player + 1]['player_id'] in self.rounds[r][4][p]):

                        player2 = score_sorted_list[player + 1]
                    else:
                        if player <= len(score_sorted_list) - 3:
                            player2 = score_sorted_list[player + 2]
            pair_sort_by_score.extend([player1, player2])
            pairs_sort_by_score.append(pair_sort_by_score)

        return pairs_sort_by_score

    def display_tournament_infos(self):  # -> Vue
        return self.tournaments

    def save_tournament(self):
        pass
