from tinydb import TinyDB, Query
from pprint import pprint


class Tournament:
    def __init__(self, name, location, date, players, time_control, notes):
        self.name = name
        self.location = location
        self.date = date
        self.players = players
        self.num_rounds = 4
        self.rounds = []
        self.time_control = time_control
        self.notes = notes
        self.tournament_is_on = False

    @property
    def serialize_tournament(self):
        serialized_tournament = {
            'name': self.name,
            'location': self.location,
            'date': self.date,
            'players': self.players,
            'num_rounds': self.num_rounds,
            'rounds': self.rounds,
            'time_control': self.time_control,
            'notes': self.notes
        }
        return serialized_tournament

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
        """sort the list of players with equal total score by their ranking. fill the list of players sorted
        by score and rank"""
        scores_list = sorted(scores_list, key=lambda k: k['rank'])  # sort by rank the equal score list
        for player in scores_list:
            new_list.append(player)  # fill the list sorted by score and rank
        return new_list

    def pairs_by_score(self):
        """Sorts list of players by score and creates 4 pairs. If scores are equals, sort by rank.
         returns a list of 4 lists of 2 players sorted by score and rank"""

        # creates a list of players sorted by their 'total score'
        score_sorted_list = sorted(self.players, key=lambda k: k['total_score'], reverse=True)
        pprint(score_sorted_list)

        # Sort by rank if equal scores
        equal_scores_list = []  # creates a list of players with equal scores
        score_rank_sort_list = []  # creates a list of sort by score and by rank if scores are equal
        for i in range(0, 8, 2):
            # if 'total score' player is equal with TS next player -> 2 players go to equal_score_list
            if score_sorted_list[i]['total_score'] == score_sorted_list[i+1]['total_score']:
                equal_scores_list.append(score_sorted_list[i])
                equal_scores_list.append(score_sorted_list[i+1])
            # if total score player NOT equal to the next one
            else:
                equal_scores_list.append(score_sorted_list[i])  # first player go to equal_score_list
                self.sort_new_list(equal_scores_list, score_rank_sort_list) # create list sorted by score and rank
                equal_scores_list.clear()
                equal_scores_list.append(score_sorted_list[i+1])  # clear the list and append the next player
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
        return pprint(self.serialize_tournament, sort_dicts=False)

    def insert_db(self, db):
        db.insert(self.serialize_tournament)

    def update_db(self, db):
        db.update({})
