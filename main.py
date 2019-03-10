import json

class Game:
  def __init__(self):
    #lettura del file game.json
    with open('game.json') as f:
      data = json.load(f)
    #creazione lista di stanze già istanziate all'interno di questa
    self.rooms = []
    self.description = data["description"]
    self.levels = int(data["levels"])
    for x in range(self.levels):
      self.rooms.append(Room(x))

class Room:
  def __init__(self, n):
    self.n = n
    self.w = 0
    self.h = 0
    #apertura file della stanza
    file = open(str(n) + ".room")
    r = file.readlines()
    file.close()
    #lettura caratteri del file e assegnazione altezza 
    l = 0
    for y in r:
      for x in y:
        if x =="\n":
          self.h += 1
        else:
          l += 1
    #assegnazione larghezza
    self.w = round(l/ self.h)

#istanziata la classe Game
game = Game()
#printata descrizione del gioco per il giocatore
print(game.description)