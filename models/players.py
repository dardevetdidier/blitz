from tinydb.operations import set


class Player:

    def __init__(self, player_id, name, first_name, birth, sex, rank, total_score):
        self.player_id = player_id
        self.name = name
        self.first_name = first_name
        self.birth = birth
        self.sex = sex
        self.rank = rank
        self.total_score = total_score

    @property
    def serialize_player(self):
        serialized_player = {
            'player_id': self.player_id,
            'name': self.name,
            'first_name': self.first_name,
            'birth': self.birth,
            'sex': self.sex,
            'rank': self.rank,
            'total_score': self.total_score
        }
        return serialized_player

    @staticmethod
    def deserialize_player(serial_player):
        player_id = serial_player['player_id']
        name = serial_player['name']
        first_name = serial_player['first_name']
        birth = serial_player['birth']
        sex = serial_player['sex']
        rank = serial_player['rank']
        total_score = serial_player['total_score']

        player = Player(player_id, name, first_name, birth, sex, rank, total_score)
        return player

    @staticmethod
    def add_player_to_db(db, query, players):
        for player in range(len(players)):
            db.update(set('total_score', players[player]['total_score']),
                      query.player_id == players[player]['player_id'])
