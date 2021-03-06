# -*- coding: utf-8 -*-
import parentpath
from console import Console
from fov import Fov
import coord
import direction

class Map(object):
  def __init__(self):
    self._map = [
        '###################################',
        '#                                 #',
        '#  # # #        ###########       #',
        '#               #                 #',
        '#  # # #        #         #       #',
        '#                         #       #',
        '#  # # #        #         #       #',
        '#               ###########       #',
        '#                                 #',
        '###################################'
        ]

  def render(self, screen):
   for y, line in enumerate(self._map):
     screen.move((0, y)).write(line)

  def isWall(self, point):
    if self.isOutBound(point):
      return True
    x, y = point
    return self._map[y][x] is '#'

  def isFloor(self, point):
    if self.isOutBound(point):
      return False
    x, y = point
    return self._map[y][x] is ' '

  def isOutBound(self, point):
    x, y = point
    return x < 0 or y < 0 or x >= len(self._map[0]) or y >= len(self._map)

  def isInBound(self, point):
    return not self.isOutBound(point)

class FovDemo(object):
  KeyMap = {
    "h": direction.W, "j": direction.S, "k": direction.N, "l": direction.E,
    "y": direction.NW, "u": direction.NE, "b": direction.SW, "n": direction.SE
  }

  def __init__(self):
    self._hero = (1, 1)
    self._console = Console()
    self._map = Map()
    self._fov = Fov(self._map.isFloor, 5)

  def run(self):
    while True:
      self.update()

  def update(self):
    self.render()
    key = self._console.getKey()
    self.moveHero(self.KeyMap.get(key, (0, 0)))

  def moveHero(self, dir):
    nextCoord = coord.sum(self._hero, dir)
    if self._map.isWall(nextCoord): return
    self._hero = nextCoord

  def render(self):
    self._console.clear()
    self._map.render(self._console)
    self.renderFov()
    self._console.move(self._hero).write("@").move(self._hero)

  def renderFov(self):
    for c in self._fov.compute(self._hero):
      if self._map.isFloor(c) and self._map.isInBound(c):
        self._console.move(c).write('.')

if __name__ == '__main__':
  FovDemo().run()

