class Entity:
  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic

class Level:
  def __init__(self, w, h):
    self.w = w
    self.h = h
    self.entities = []

  def add_entities(self, entities):
    self.entities += entities

  def draw(self):
    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if e.x == x and e.y == y:
            print("[{}]".format(e.graphic), end = "")
            break
        else:
          print("[ ]", end = "")

      print()

player = Entity(1, 3, "P")
monster = Entity(3, 4, "M")
level = Level(10, 10)

level.add_entities([player, monster])

level.draw()