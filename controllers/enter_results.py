def enter_results(player1, player2):
    """User enters results of the round. Returns Tuple of 2 lists ([player1, score1], [player2, score2])"""
    player1_score = 0.1
    player2_score = 0.1
    score_list = [0.0, 0.5, 1.0]

    while not (player1_score + player2_score == 1 and player1_score in score_list and player2_score in score_list):
        player1_score = float(input(f"\n\tEntrez le score de {player1['name']} {player1['first_name']} : "))
        player2_score = float(input(f"\tEntrez le score de {player2['name']} {player2['first_name']} : "))

    player1['total_score'] += player1_score
    player2['total_score'] += player2_score
    result = ([f"player {player1['player_id']}", player1_score],
              [f"player {player2['player_id']}", player2_score])
    return result
