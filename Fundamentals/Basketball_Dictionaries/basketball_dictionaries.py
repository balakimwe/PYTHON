
# Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.age = player_dict['age']
        self.position = player_dict['position']
        self.team = player_dict['team']
    
    # Preference on how to display class in the console after printing
    def __repr__(self):
        display = f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"
        return display


kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}

jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}


kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}


Player_Kevin = Player(kevin)
print(Player_Kevin)


player_jason = Player(jason)
print(player_jason)

player_kyrie = Player(kyrie)
print(player_kyrie)


# Finally, given the example list of players at the top of this module (the one with many players) write a for loop that will populate an empty list with Player objects from the original list of dictionaries.


players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# For loop over the list of dictionaries

new_team = []
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

    print(new_team)



  # * BONUS class mehotd

    @classmethod
    def add_players(cls, player_dict):
        new_team = []
        for player_dict in players:
            new_team.append(cls(player_dict))
        return new_team