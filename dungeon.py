# -*- coding: utf-8 -*-
from cellular import Cellular
import direction
import coord
import random

class Space(object):
  def __init__(self, size):
    self._size = size
    self._space = set()
    self._exitCanditate = []

  def __iter__(self):
    w, h = self._size
    for y in range(h):
      for x in range(w):
        yield (x, y)

  @property
  def spaces(self):
    return self._space.copy()

  @property
  def exitCanditate(self):
    return self._exitCanditate[:]

  def build(self):
    self.dig()
    self.updateExitCanditate()
    return self

  def updateExitCanditate(self):
    for w in self._walls():
      if len([d for d in direction.CROSS if coord.sum(w, d) in self._space]) != 1: continue
      self._exitCanditate.append(w)

  def move(self, point):
    self._space = set([coord.sum(point, s) for s in self._space])
    return self

  def _walls(self):
    walls = set()
    for p in self._space:
      walls |= set([w for w in [coord.sum(p, d) for d in direction.CROSS] if w not in self._space])
    return walls

class SquareSpace(Space):
  def dig(self):
    w, h = self._size
    for x, y in self:
      if x == 0 or y == 0 or x == w - 1 or y == h - 1: continue
      self._space.add((x, y))
    return self

class CrossSpace(Space):
  def dig(self):
    w, h = self._size
    vw, vh = random.randrange(4, w - 2), h
    hw, hh = w, random.randrange(4, h - 2)
    vx = random.randrange(0, w - vw + 1)
    hy = random.randrange(0, h - hh + 1)
    self._space |= SquareSpace((vw, vh)).dig().move((vx, 0)).spaces
    self._space |= SquareSpace((hw, hh)).dig().move((0, hy)).spaces

class CircleSpace(Space):
  def dig(self):
    w, h = self._size
    cx, cy = int(w/2), int(h/2)
    r = min(self._size) / 2
    for x, y in self:
      if (x-cx)**2 + (y-cy)**2 < r**2:
        self._space.add((x, y))

class OrganicSpace(Space):
  def dig(self):
    self._space = Cellular(self._size).initialize(45).update(5, 3, 5).areas().biggestArea()
    if not self._space: self._space = set()
    return self

class Dungeon(object):
  def __init__(self, size):
    self._size = size
    self._exits = []
    self._space = set()

  def __iter__(self):
    for c in self._space:
      yield c

  @property
  def exits(self):
    return self._exits[:]

  def generate(self):
    # self.addRoom(OrganicSpace((20, 20)).build())
    # self.addRoom(SquareSpace((13, 5)).build())
    # self.addRoom(CrossSpace((13, 10)).build())
    self.addRoom(CircleSpace((10, 10)).build())
    return self

  def addRoom(self, room):
    self._space |= room.spaces
    self._exits.extend(room.exitCanditate)

from matrix import Matrix
class DungeonDemo(object):
  def __init__(self):
    self._size = (80, 20)
    self._map = Matrix(self._size, "#")

  def run(self):
    dungeon = Dungeon(self._size).generate()
    for c in dungeon:
      self._map.put(c, ".")
    self.show()
    input()
    for e in dungeon.exits:
      self._map.put(e, "+")
    self.show()

  def show(self):
    for line in self._map.lines:
      print(''.join([c for c in line]))

if __name__ == '__main__':
  DungeonDemo().run()

