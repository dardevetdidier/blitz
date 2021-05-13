from models.players import Player

#
# def generates_players():
#     """User enters informations of 8 players. returns list of 8 players"""
#     players = []
#     for i in range(1, 3):
#         print(f"\nEntrez les informations du joueur {i} :\n ")
#         player_id = i
#         name = input("Nom : ")
#         first_name = input("Prénom : ")
#         birth = input("Date de naissance : ")
#         sex = input("Sexe : ")
#         rank = int(input("Classement : "))
#         player = Player(player_id, name, first_name, birth, sex, rank).player
#         # player.save_player()
#         players.append(player)
#     print(players)
#     return players
