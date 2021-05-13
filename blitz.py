# from controllers.launch_tournament import launch_tournament
from models.tournament import Tournament
from test import *

launch_tournament()
pairs = StartingAllPairs().starting_pairs_list
print(pairs)

#
# pprint.pprint(pairs, sort_dicts=False)


# pprint.pprint(sort_by_rank(), sort_dicts=False)
# match = Match()
# print(match.enter_result())

# pairs = StartingPair()
# print(pairs.starting_pair)
# ajouter joueur à la base de donnée


# TODO 2 : Créer paire de joueurs -> système suisse

# TODO 3 : Créer résultats avec (inputs) -> fichier json ?
