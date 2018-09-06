# -*- coding: utf-8 -*-
import parentpath
import random
from matrix import Matrix
from generator import Generator

class GeneratorDemo(object):
  def __init__(self, size):
    self._generator = Generator(size).setDeadEnd(3).generate()
    self._map = Matrix(size, ' ')

  def apply(self):
    self.applyMap()
    self.putStairsAndTreasure()
    self.putMonsterToRoom()
    return self

  def applyMap(self):
    for (c, t) in self._generator:
      self._map.put(c, t.ch)

  def putStairsAndTreasure(self):
    deadends = [de for de in self._generator.deadends]
    random.shuffle(deadends)
    self._map.put(deadends[0], '>')
    self._map.put(deadends[1], '<')
    self._map.put(deadends[2], '$')

  def putMonsterToRoom(self):
    for room in self._generator.room:
      inside = room.shurink(1)
      for c in inside:
        if random.randint(0, 2):
          self._map.put(c, random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

  def show(self):
    for line in self._map.lines:
      print(''.join([c for c in line]))

if __name__ == '__main__':
  GeneratorDemo((79, 21)).apply().show()
