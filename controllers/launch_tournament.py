from models.tournament import Tournament


def launch_tournament(players):
    """User enters informations of tournament and instances players"""
    time_control_list = ["bullet", "blitz", "coup rapide"]
    time_control = ''
    name = input("Nom du tournoi : ")
    location = 'ici'  # input("Lieu du tournoi :  ")
    date = '12/12/2021'  # input("Date du tournoi : ")
    rounds = []
    while time_control not in time_control_list:
        time_control = 'bullet'  # input("'bullet', 'blitz' ou 'coup rapide'? : ").lower()
    notes = 'RAS'  # input("Remarques du directeur : ")

    tournament = Tournament(name, location, date, players, rounds, time_control, notes)
    tournament.tournament_is_on = True
    return tournament
