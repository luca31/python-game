import json

class Game:
  def __init__(self):
    with open('game.json') as f:
      data = json.load(f)

    self.rooms = []
    self.description = data["description"]
    self.levels = int(data["levels"])
    for x in range(self.levels):
      self.rooms.append(Room(x))

class Room:
  def __init__(self, n):
    self.n = n
    # leggere il file n.room


game = Game()

print(game.description)