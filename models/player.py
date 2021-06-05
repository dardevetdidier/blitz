from tinydb import TinyDB


class Player:

    def __init__(self, player_id, name, first_name, birth, sex, rank, total_score):
        self.player_id = player_id
        self.name = name
        self.first_name = first_name
        self.birth = birth
        self.sex = sex
        self.rank = rank
        self.total_score = total_score
        self.players_db = TinyDB('players.json', encoding='utf-8', ensure_ascii=False, indent=4)

    @property
    def serialize_player(self):
        """
        serialize player from player instance
        """
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

    def add_player_to_db(self):
        """
        Add a player serialized in players' database"
        """
        self.players_db.insert(self.serialize_player)
