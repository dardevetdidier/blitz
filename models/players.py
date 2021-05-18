import json


class Player:

    def __init__(self, player_id, name, first_name, birth, sex, rank, ):
        self.player_id = player_id
        self.name = name
        self.first_name = first_name
        self.birth = birth
        self.sex = sex
        self.rank = rank
        self.total_score = 0

        self.player = {
            'player_id': self.player_id,
            'name': self.name,
            'first_name': self.first_name,
            'birth': self.birth,
            'sex': self.sex,
            'rank': self.rank,
            'total_score': self.total_score
        }

    def add_player_to_db(self):
        pass

    def save_player(self):
        """load json file, add player (dict) into file return the list of all players"""
        with open("players.json", "r", encoding="utf-8") as f:
            players = json.load(f)

        players.append(self.player)

        with open('players.json', "w", encoding="utf-8") as f:
            json.dump(players, f, indent=4, ensure_ascii=False)
