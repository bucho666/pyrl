import random
import coord
import direction
from matrix import Matrix

class Areas(object):
  def __init__(self, areas):
    self._areas = areas

  def __iter__(self):
    for area in self._areas:
      for c in area:
        yield c

  def connect(self):
    areas = self._areas[:]
    biggestArea = self.biggestArea()
    areas.remove(biggestArea)
    biggestArea = list(biggestArea)
    tunnel = set()
    for area in areas:
      for c in coord.line(random.choice(list(area)), random.choice(biggestArea)):
        tunnel.add(c)
    self._areas.append(tunnel)
    return self

  def biggestArea(self):
    biggestArea = []
    for area in self._areas:
      if len(area) > len(biggestArea):
        biggestArea = area
    return biggestArea

class Cellular(object):
  def __init__(self, size):
    self._width, self._height = size
    self._alives = set();

  def __iter__(self):
    for c in self._alives:
      yield c

  def initialize(self, birthProbability):
    for c in self._cells():
      if random.randint(0, 99) < birthProbability:
        self._alives.add(c)
    return self

  def update(self, repeat, surviveLimit, birthLimit):
    for r in range(repeat):
      self.iterate(surviveLimit, birthLimit)
    return self

  def iterate(self, surviveLimit, birthLimit):
    nextGeneration = set();
    for c in self._cells():
      if self._isFrame(c):
        nextGeneration.add(c)
        continue
      walls = self.countLiveNeighbours(c)
      if c in self._alives and walls >= surviveLimit:
        nextGeneration.add(c)
      if c not in self._alives and walls >= birthLimit:
        nextGeneration.add(c)
    self._alives = nextGeneration

  def countLiveNeighbours(self, c):
    alives = 0
    for d in direction.CIRCLE:
      if coord.sum(c, d) in self._alives:
        alives += 1
    return alives

  def areas(self):
    areas = []
    flooded = set()
    for c in self._cells():
      if c in self._alives: continue
      if c in flooded: continue
      area = self.flood(c, set([c]))
      areas.append(area)
      flooded |= area
    return Areas(areas)

  def flood(self, start, flooded):
    for d in direction.CIRCLE:
      c = coord.sum(start, d)
      if self._isOutBound(c): continue
      if c in self._alives: continue
      if c in flooded: continue
      flooded.add(c)
      self.flood(c, flooded)
    return flooded

  def _cells(self):
    for y in range(self._height):
      for x in range(self._width):
        yield (x, y)

  def _isFrame(self, point):
    x, y = point
    return x == 0 or y == 0 or x == self._width - 1 or y == self._height - 1

  def _isOutBound(self, point):
    x, y = point
    return x < 0 or y < 0 or x >= self._width or y >= self._height
