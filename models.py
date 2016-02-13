import db

class Player(object):
    """
    db model for players
    """
    collection = None

    def __init__(self, name, surname, rank):
        self.name = name
        self.surname = surname
        self.rank = rank

    @classmethod
    def get_collection(self):
        return db.user_db.player

    @classmethod
    def find(cls, criteria=None):
        criteria = criteria or {}
        player_list = []
        for player_data in cls.get_collection().find(criteria):
            player_list.append(Player(player_data['name'], player_data.get('surname'), player_data.get('rank')))
        return player_list

    @classmethod
    def get(cls, criteria):
        criteria = criteria or {}
        player_data = cls.get_collection().find_one(criteria)
        return Player(player_data['name'], player_data.get('surname'), player_data.get('rank'))

    @classmethod
    def create(cls, player_data):
        if not player_data.get('name'):
            raise AttributeError('player name is required')
        player_id = cls.get_collection().insert(player_data)
        return cls.get({"_id": player_id})
