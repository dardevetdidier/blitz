# from controllers.generates_rounds import generates_starting_round
# from controllers.generates_players import generates_players


class Tournament:
    def __init__(self, name, location, date, time_control, notes):
        self.name = name
        self.location = location
        self.date = date
        self.players = []
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
        # print(self.tournaments)

    def display_tournament_infos(self):
        print(self.tournaments)
