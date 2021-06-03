from time import strftime, localtime
from os import system


class Round:

    def __init__(self, players_pairs):
        self.name = ''
        self.start_time = None  # changes when round is created
        self.end_time = None  # changes when round is over
        self.players_pairs = players_pairs
        self.scores = None
        self.round_list = []

    def starts_round(self, round_number, tournament):
        """
        Modifies 'name' and 'start_time' attributs, used by the new instance creation when user creates a new round.
        Returns a list containing round information
        """
        self.name = f"round_{round_number}"
        self.start_time = strftime('%a %d %b %Y %H:%M:%S', localtime())
        self.round_list.extend([self.name, self.start_time, self.end_time, self.players_pairs, self.scores])
        system('cls')
        print(f"\n\tLe round {round_number} du tournoi '{tournament}' a bien été créé.")
        return self.round_list

    def ends_round(self, scores):
        """
        modifies the date of the end of the round. Modifies end date of the round and scores entered by user in round
        list. Returns this list.
        """
        self.end_time = strftime('%a %d %b %Y %H:%M:%S', localtime())
        self.round_list[2] = self.end_time
        self.round_list[-1] = scores
        return self.round_list
