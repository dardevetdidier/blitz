from tinydb import TinyDB, Query
from tinydb.operations import set
from controllers.press_to_clear import enter_to_clear


class Tournament:
    """object Tournament"""
    def __init__(self, name, location, date, players, rounds, time_control, notes):
        self.name = name
        self.location = location
        self.date = date
        self.players = players
        self.num_rounds = 4
        self.rounds = rounds
        self.time_control = time_control
        self.notes = notes
        self.tournament_is_on = False
        self.tournaments_db = TinyDB('tournaments.json', encoding='utf-8', ensure_ascii=False, indent=4)
        self.players_db = TinyDB('players.json', encoding='utf-8', ensure_ascii=False, indent=4)

    @property
    def serialize_tournament(self):
        """Serializes object tournament to a dictionnary"""
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

    @staticmethod
    def deserialize_tournament(serial_tournament):
        """deserializes each attribut of 'tournament' object and returns an instance of Tournament object"""
        name = serial_tournament['name']
        location = serial_tournament['location']
        date = serial_tournament['date']
        players = serial_tournament['players']
        rounds = serial_tournament['rounds']
        time_control = serial_tournament['time_control']
        notes = serial_tournament['notes']

        tournament = Tournament(name, location, date, players, rounds, time_control, notes)
        return tournament

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

        # Sort by rank if equal scores
        equal_scores_list = []  # creates an empty temporary list of players with equal scores
        score_rank_sort_list = []  # creates an empty list of sort by score and by rank players if scores are equal

        while len(score_rank_sort_list) < self.num_rounds * 2:
            counter = scores_list.count(scores_list[0])  # returns how many players with the first score of the list

            for i in range(counter):
                equal_scores_list.append(score_sorted_list[0])  # add player with first score in the list
                del score_sorted_list[0]  # delete the first occurence of the list
                del scores_list[0]  # delete the first occurence of the score list

            # definitive list is sorted with 'sort_new_list' function
            score_rank_sort_list = self.sort_new_list(equal_scores_list, score_rank_sort_list)

            equal_scores_list.clear()  # clear the temporary list

        return score_rank_sort_list

    def already_played(self, list_by_score):
        """ Returns true if a player has already play with the next one"""
        for player in range(0, 8, 2):
            for r in range(len(self.rounds)):  # iter in the tournament list of rounds
                for p in range(len(self.rounds[r][4])):  # iter in the list of tuples
                    if (list_by_score[player]['player_id'] in self.rounds[r][4][p] and list_by_score[player + 1]
                            ['player_id'] in self.rounds[r][4][p]):
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
                    list_by_score[player + 2] = list_by_score[player + 1]  # P+1 replace P+2
            else:
                player2 = list_by_score[player + 1]

            pair_sort_by_score.extend([player1, player2])
            pairs_sort_by_score.append(pair_sort_by_score)
        return pairs_sort_by_score

    def insert_db(self):
        """ writes tournament information in tournament.json file"""
        self.tournaments_db.insert(self.serialize_tournament)
        print("\t\nLes informations du tournoi ont bien été enregistrées.")
        enter_to_clear()

    def update_tournament_db(self, serial_tournament):
        """ Updates 'rounds' and 'players' values in tournament.json file"""
        query = Query()
        self.tournaments_db.update({'rounds': self.rounds}, query.name == serial_tournament['name'])
        self.tournaments_db.update({'players': self.players}, query.name == serial_tournament['name'])

    def update_players_score(self):
        """ Updates 'total_score' values of the players of a tournament in tournament.json file"""
        query = Query()
        for player in range(len(self.players)):
            self.players_db.update(set('total_score', self.players[player]['total_score']),
                                   query.player_id == self.players[player]['player_id'])

    def switch_tournament_on(self, round_nb):
        """ Assign 'True' value to attribut 'tournament_is_on'"""
        if not round_nb > self.num_rounds:
            self.tournament_is_on = True
