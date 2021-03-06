# -*- coding: utf-8 -*-
import parentpath
import coord
import direction
from console import Console
from astar import AStar

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
     screen.move((0, y)).write(''.join(line))

  def put(self, coord, terrain):
    x, y = coord
    self._map[y][x] = terrain

  def cost(self, coord):
    if self.isOutBound(coord): return 255
    x, y = coord
    terrain = self._map[y][x]
    if terrain == '#': return 99
    if terrain == '=': return 10
    if terrain == '"': return 2
    if terrain == ' ': return 1
    return 255

  def isOutBound(self, coord):
    x, y = coord
    return x < 0 or y < 0 or x >= len(self._map[0]) or y >= len(self._map)

  def isInBound(self, coord):
    return not self.isOutBound(coord)

class AStarDemo(object):
  KeyMap = {
    "h": direction.W, "j": direction.S, "k": direction.N, "l": direction.E,
    "y": direction.NW, "u": direction.NE, "b": direction.SW, "n": direction.SE
  }

  def __init__(self):
    self._cursor = (1, 1)
    self._start = (1, 1)
    self._goal = (33, 8)
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
      self._cursor = coord.sum(self._cursor, self.KeyMap.get(key))
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
