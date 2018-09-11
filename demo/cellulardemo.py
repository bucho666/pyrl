# -*- coding: utf-8 -*-
import parentpath
from cellular import Cellular
from matrix import Matrix

class Cave(object):
  def __init__(self, size):
    self._map = Matrix(size, '#')

  def dig(self):
    areas = Cellular(self._map.size).initialize(40).update(5, 3, 5).areas().connect()
    for c in areas:
      self._map.put(c, '.')
    return self

  def show(self):
    for line in self._map.lines:
      print(''.join([c for c in line]))

if __name__ == '__main__':
  Cave((80, 20)).dig().show()
