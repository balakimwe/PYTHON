from players import players

class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']

        player1 = Player(players[0])
        Player2 = Player()

