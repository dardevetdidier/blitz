from models.pairs import sort_by_rank


class FirstRound:
    def __init__(self, name, start_time):
        self.round_name = name
        self.start_time = start_time
        self.end_time = None  # changes when enters results
        self.pairs = sort_by_rank()

    def enter_results(self):
        """enter results and return tuple [(player1, score1), (player2, score2)]"""
        pass

    def display_round_infos(self):
        pass
