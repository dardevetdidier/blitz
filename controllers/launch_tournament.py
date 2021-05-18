from models.tournament import Tournament
from controllers.generates_players import generates_players


def launch_tournament():
    """User enters informations of tournament and instances players"""
    name = 'tournoi 1'  # input("Nom du tournoi : ")
    location = 'ici'  # input("Lieu du tournoi :  ")
    date = '12/12/2021'  # input("Date du tournoi : ")
    time_control = 'Bullet'  # input("'Bullet', 'Blitz' ou 'Coup rapide'? : ")
    notes = 'RAS'  # input("Remarques du directeur : ")

    players = generates_players()
    tournament = Tournament(name, location, date, players, time_control, notes)
    # tournament.pairs_by_rank()
    # pprint.pprint(tournament.pairs_by_rank())
    # tournament.display_tournament_infos()
    # with open('tournament.json', "w") as f:
    #     json.dump(tournament.tournaments, f, indent=4, ensure_ascii=False)
    return tournament
