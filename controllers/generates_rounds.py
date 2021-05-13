from models.rounds import FirstRound
from time import localtime, strftime


def generates_starting_round():
    rounds = []

    name = f"round1"
    start_time = strftime("%a %d %b %Y %H:%M:%S", localtime())

    round_ = FirstRound(name, start_time)
    return rounds.append(round_)
