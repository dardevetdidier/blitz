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

    @staticmethod
    def sort_new_list(scores_list, new_list):
        scores_list = sorted(scores_list, key=lambda k: k['rank'])
        for player in scores_list:
            new_list.append(player)
        return new_list

    def pairs_by_score(self):
        """Sorts list of players by score and creates 4 pairs. If scores are equals, sort by rank.
         returns a list of 4 lists of 2 players sorted by score and rank"""

        score_sorted_list = sorted(self.players, key=lambda k: k['total_score'], reverse=True)
        # Sort by rank if equal scores
        equal_scores_list = []
        score_rank_sort_list = []
        for i in range(0, 8, 2):
            if score_sorted_list[i]['total_score'] == score_sorted_list[i+1]['total_score']:
                equal_scores_list.append(score_sorted_list[i])
                equal_scores_list.append(score_sorted_list[i+1])
            else:
                equal_scores_list.append(score_sorted_list[i])
                self.sort_new_list(equal_scores_list, score_rank_sort_list)
                equal_scores_list.clear()
                equal_scores_list.append(score_sorted_list[i+1])
        score_sorted_list = self.sort_new_list(equal_scores_list, score_rank_sort_list)

        # create pairs
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
