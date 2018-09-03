import random
from matrix import Matrix
from size import Size
import direction

class Cellular(object):
  def __init__(self, size):
    self._map = Matrix(size, True)

  def __iter__(self):
    for c in self._map:
      yield c

  @property
  def lines(self):
    for line in self._map.lines:
      yield line

  def initialize(self, birthProbability):
    for c in self._map:
      self._map.put(c, random.randint(0, 99) < birthProbability)
    return self

  def connect(self):
    areas = self.areas()
    biggestArea = []
    for area in areas:
      if len(area) > len(biggestArea):
        biggestArea = area
    areas.remove(biggestArea)
    biggestArea = list(biggestArea)
    for area in areas:
      for c in random.choice(list(area)).toLine(random.choice(biggestArea)):
        self._map.put(c, False)
    return self

  def areas(self):
    areas = []
    flooded = set()
    for c in self._map:
      if self._map.at(c): continue
      if c in flooded: continue
      area = self.flood(c, set([c]))
      areas.append(area)
      flooded |= area
    return areas

  def flood(self, coord, flooded):
    for d in direction.AROUND:
      c = coord + d
      if self._map.isOutBound(c): continue
      if self._map.at(c) == True: continue
      if c in flooded: continue
      flooded.add(c)
      self.flood(c, flooded)
    return flooded

  def update(self, repeat, surviveLimit, birthLimit):
    for r in range(repeat):
      self.iterate(surviveLimit, birthLimit)
    return self

  def iterate(self, surviveLimit, birthLimit):
    nextGeneration = Matrix(self._map.size)
    for c in self._map:
      walls = self.countLiveNeighbours(c)
      if self._map.at(c):
        nextGeneration.put(c, walls >= surviveLimit)
      else:
        nextGeneration.put(c, walls >= birthLimit)
    self._map = nextGeneration

  def countLiveNeighbours(self, c):
    walls = 0
    for d in direction.AROUND:
      ac = c + d
      if self._map.isOutBound(ac): return 9
      if self._map.at(ac):
        walls += 1
    return walls
