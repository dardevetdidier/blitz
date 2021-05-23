from time import strftime, localtime
from os import system
# from blitz import tournament
# from views.menu import display_tournament_menu


class Round:

    def __init__(self, players_pairs):
        self.name = ''
        self.start_time = None  # changes when round is created
        self.end_time = None  # changes when round is over
        self.players_pairs = players_pairs
        self.scores = None
        # self.round_number = len(self.round_list) + 1
        # self.round_is_on = False
        # self.round_is_over = True
        self.round_list = []

    def starts_round(self, round_number):
        # self.round_is_on = True
        self.name = f"round_{round_number}"
        self.start_time = f"Début : {strftime('%a %d %b %Y %H:%M:%S', localtime())}"
        self.round_list.extend([self.name, self.start_time, self.end_time, self.players_pairs, self.scores])
        system('cls')
        print(f"\n\tLe round {round_number} a bien été créé.")
        return self.round_list

    def ends_round(self, scores):
        print(self.round_list)
        self.end_time = f"Fin : {strftime('%a %d %b %Y %H:%M:%S', localtime())}"
        self.round_list[2] = self.end_time
        self.round_list[-1] = scores
        return self.round_list

    def display_round_infos(self):
        pass
