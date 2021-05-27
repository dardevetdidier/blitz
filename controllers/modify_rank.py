from tinydb.operations import set


def modify_rank(db, query, players):
    id_player_to_modify = 0
    while True:
        try:
            id_player_to_modify = int(input("\n\t    --> Entrer l'identifiant du joueur à modifier: "))
            if id_player_to_modify in range(1, len(players) + 1):
                break
        except ValueError:
            continue

    player_to_modify = db.search(query.player_id == id_player_to_modify)
    name_p_to_modify = player_to_modify[0]['first_name'] + " " + player_to_modify[0]['name']

    new_rank = int(input(f"\n\t    --> Entrer le nouveau classement de {name_p_to_modify}: "))

    db.update(set('rank', new_rank), query.player_id == id_player_to_modify)
    print("\n\t\t*** Le classement du joueur a été mis à jour ***")
