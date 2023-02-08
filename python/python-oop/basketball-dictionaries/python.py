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

class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]
    
    @classmethod
    def get_team(cls, team_list):
      new_list = []
      for player in team_list:
        new_list.append(player)
      return new_list

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
  "age":32,
    "position": "Point Guard", 
  "team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

new_team = []
for player in players:
  new_team.append(Player(player))

print(Player.get_team(players))