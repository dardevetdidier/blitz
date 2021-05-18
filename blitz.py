from controllers.launch_tournament import launch_tournament
from controllers.enter_results import enter_results
from models.rounds import Round
from pprint import pprint


# ***************** --> MAIN *****************************
# créer un tournoi
tournament_1 = launch_tournament()  # ---> objet tournament
tournament_1.display_tournament_infos()

# crée les paires selon le classement
pairs_sort_rank = tournament_1.pairs_by_rank()
print(f"\npaires triées par classement:\n")
pprint(pairs_sort_rank, sort_dicts=False)

# crée le premier tour
round_1 = Round(pairs_sort_rank)
print(f"\nCreation du round 1:\n")
pprint(round_1.starts_round(tournament_1.num_rounds), sort_dicts=False)

# entrer les résultats
results_list = []
for i in range(len(pairs_sort_rank)):
    results = enter_results(pairs_sort_rank[i][0], pairs_sort_rank[i][-1])
    results_list.append(results)

# affiche la liste des resultats par pairs
print(f"Resultats par pairs:\n")
pprint(results_list)

# affiche le round terminé
print(f"\nInfos du round:\n")
round_ended = round_1.ends_round(results_list)
pprint(round_ended, sort_dicts=False)

# envoie les infos du round dans l'attribut rounds de la classe tournament
tournament_1.tournaments['rounds'].append(round_ended)

# affiche les infos du tournoi
print(f"\ninfos du tournoi:\n")
pprint(tournament_1.display_tournament_infos(), sort_dicts=False)

# affiche la liste des joueurs triés par score total
print(f"\nListe des joueurs triés par score :\n")
pprint(tournament_1.pairs_by_score(), sort_dicts=False)




# TODO : améliorer la creation de paires : si meme score total > classer par rang

