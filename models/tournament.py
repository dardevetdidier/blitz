from pprint import pprint
from collections import Counter


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

    def sort_by_score(self):
        """Sorts list of players by score and creates 4 pairs. If scores are equals, sort by rank.
         returns a list of 4 lists of 2 players sorted by score and rank"""

        # creates a list of players sorted by their 'total score'
        score_sorted_list = sorted(self.players, key=lambda k: k['total_score'], reverse=True)

        # creates a list of the scores to count how many of each score
        scores_list = []
        for i in range(len(score_sorted_list)):
            scores_list.append(score_sorted_list[i]['total_score'])

        print(scores_list)

        # Sort by rank if equal scores
        equal_scores_list = []  # creates an empty temporary list of players with equal scores
        score_rank_sort_list = []  # creates an empty list of sort by score and by rank players if scores are equal

        while len(score_rank_sort_list) < self.num_rounds * 2:
            counter = scores_list.count(scores_list[0])  # returns how many players with the first score of the list
            # print(score_sorted_list[0]['total_score'])
            print(counter)

            for i in range(counter):
                equal_scores_list.append(score_sorted_list[0])  # add player with first score in the list
                del score_sorted_list[0]  # delete the first occurence of the list
                del scores_list[0]  # delete the first occurence of the score list
            # definitive list is sorted with 'sort_new_list' function
            score_rank_sort_list = self.sort_new_list(equal_scores_list, score_rank_sort_list)

            equal_scores_list.clear()  # clear the temporary list

        pprint(score_rank_sort_list, sort_dicts=False)

        return score_rank_sort_list



        # for i in range(0, self.num_rounds*2, 2):
        #     # if 'total score' player is equal with TS next player -> 2 players go to equal_score_list
        #     if score_sorted_list[i]['total_score'] == score_sorted_list[i + 1]['total_score']:
        #         score_rank_sort_list = sorted(score_rank_sort_list, key=lambda k: k['rank'])
        #         equal_scores_list.append(score_sorted_list[i])
        #         equal_scores_list.append(score_sorted_list[i + 1])
        #         print(f"equal score list : {equal_scores_list}")
        #         if not i == len(score_sorted_list) - 3:
        #             if not score_sorted_list[i+1]['total_score'] == score_sorted_list[i+2]['total_score']:
        #                 score_rank_sort_list = self.sort_new_list(equal_scores_list, score_rank_sort_list)
        #                 equal_scores_list.clear()
        #             else:
        #
        #
        #         elif i == len(score_sorted_list) - 3:
        #             if not score_sorted_list[i + 1] == score_sorted_list[i + 2]:
        #                 score_rank_sort_list = self.sort_new_list(equal_scores_list, score_rank_sort_list)
        #                 score_rank_sort_list.append(score_sorted_list[i + 2])
        #     # if total score player NOT equal to the next one
        #     else:
        #         score_rank_sort_list.append(score_sorted_list[i])
        #         score_rank_sort_list.append(score_sorted_list[i + 1])
        #         # equal_scores_list.append(score_sorted_list[i])  # first player go to equal_score_list
        #         # # create list sorted by score and rank
        #         # score_rank_sort_list = self.sort_new_list(equal_scores_list, score_rank_sort_list)
        #         # equal_scores_list.clear()
        #         # equal_scores_list.append(score_sorted_list[i + 1])  # clear the list and append the next player
        # self.sort_new_list(equal_scores_list, score_rank_sort_list)
        # pprint(f"score sorted list : {score_rank_sort_list}")



        # return score_rank_sort_list

    def already_played(self, list_by_score):
        """ Returns true if a player has already play with the next one"""
        for player in range(0, 8, 2):
            for r in range(len(self.rounds)):  # iter in the tournament list of rounds
                for p in range(len(self.rounds[r][4])):  # iter in the list of tuples
                    if (list_by_score[player]['player_id'] in self.rounds[r][4][p] and
                            list_by_score[player + 1]['player_id'] in self.rounds[r][4][p]):
                        return True
                    else:
                        return False

    def pairs_by_score(self, list_by_score):
        """Returns a list of pairs of players sorted by score and by rank if players have already played together"""
        # create pairs
        pairs_sort_by_score = []
        player2 = {}
        for player in range(0, 8, 2):
            pair_sort_by_score = []
            player1 = list_by_score[player]

            if self.already_played(list_by_score):
                if player <= len(list_by_score) - 3:
                    player2 = list_by_score[player + 2]
            else:
                player2 = list_by_score[player + 1]

            pair_sort_by_score.extend([player1, player2])
            pairs_sort_by_score.append(pair_sort_by_score)

        return pairs_sort_by_score

    def display_tournament_infos(self):  # -> Vue
        return pprint(self.serialize_tournament, sort_dicts=False)

    def insert_db(self, db):
        db.insert(self.serialize_tournament)

    # def update_db(self, db):
    #     db.update({})
