# -*- coding: utf-8 -*-
import parentpath
from console import Console
from coord import Coord
from astar import AStar
import direction

class Map(object):
  def __init__(self):
    self._map = [
        list('###################################'),
        list('#S    " #           ##===####     #'),
        list('###   ""#      #""  ##== ###   =  #'),
        list('##    ""#    ###"""=#=== ##   ==  #'),
        list('#= ="=""##    ####"==    ##   ==  #'),
        list('# ==""=""##    ###  ==#  #   ==   #'),
        list('# ==="=""##    ### ==##      ==   #'),
        list('#      ""#    ### == ##     ===   #'),
        list('#             ## =  ##     ===   G#'),
        list('###################################')
        ]

  def render(self, screen):
   for y, line in enumerate(self._map):
     screen.move(Coord(0, y)).write(''.join(line))

  def put(self, coord, terrain):
    self._map[coord.y][coord.x] = terrain

  def cost(self, coord):
    if self.isOutBound(coord): return 255
    terrain = self._map[coord.y][coord.x]
    if terrain == '#': return 99
    if terrain == '=': return 10
    if terrain == '"': return 2
    if terrain == ' ': return 1
    return 255

  def isOutBound(self, coord):
    return coord.x < 0 or coord.y < 0 or\
           coord.x >= len(self._map[0]) or coord.y >= len(self._map)

  def isInBound(self, coord):
    return not self.isOutBound(coord)

class AStarDemo(object):
  KeyMap = {
    "h": direction.W, "j": direction.S, "k": direction.N, "l": direction.E,
    "y": direction.NW, "u": direction.NE, "b": direction.SW, "n": direction.SE
  }

  def __init__(self):
    self._cursor = Coord(1, 1)
    self._start = Coord(1, 1)
    self._goal = Coord(33, 8)
    self._console = Console()
    self._map = Map()
    self._astar = AStar(self._map.cost)

  def run(self):
    while True:
      self.update()

  def update(self):
    self.render()
    key = self._console.getKey()
    if key in self.KeyMap:
      self._cursor += self.KeyMap.get(key)
    else:
      self.putTerrain(key)

  def putTerrain(self, key):
    if key not in (' ', '"', '=', '#') : return
    self._map.put(self._cursor, key)

  def render(self):
    self._console.clear()
    self._map.render(self._console)
    self._renderRoute()
    self._console.move(self._cursor)

  def _renderRoute(self):
    for c in self._astar.compute(self._start, self._goal):
      self._console.move(c).write('*')

if __name__ == '__main__':
  AStarDemo().run()

