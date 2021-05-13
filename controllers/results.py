# class Results:
#     def __init__(self, player1, player2):
#         for index in range(0, 1):
#             self.player1 = player1  # sort_by_rank()[index]
#             self.player2 = player2  # sort_by_rank()[index + 4]
#         self.player1_score = 0
#         self.player2_score = 0
#
#     def enter_results(self):
#         self.player1_score = int(input(f"\nEntrez le score de {self.player1['nom']} {self.player1['prenom']} : "))
#         self.player2_score = int(input(f"Entrez le score de {self.player2['nom']} {self.player2['prenom']} : \n"))
#         results = ([f"{self.player1['nom']} {self.player1['prenom']}", self.player1_score],
#                    [f"{self.player2['nom']} {self.player2['prenom']}", self.player2_score])
#         return results
