from models.tournament import Tournament


def launch_tournament(players):
    """User enters informations of tournament and instances players"""
    time_control_list = ["bullet", "blitz", "coup rapide"]
    time_control = ''
    print("\n\tEntrez les informations du tournoi:\n")
    name = input("Nom du tournoi : ")
    location = input("\nLieu du tournoi :  ")
    date = input("\nDate du tournoi : ")
    rounds = []
    while time_control not in time_control_list:
        time_control = input("\n'bullet', 'blitz' ou 'coup rapide'? : ").lower()
    notes = input("\nRemarques du directeur : ")

    tournament = Tournament(name, location, date, players, rounds, time_control, notes)
    tournament.tournament_is_on = True
    return tournament
