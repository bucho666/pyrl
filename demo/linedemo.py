# -*- coding: utf-8 -*-
import parentpath
import coord
import direction
from console import Console

class LineDemo(object):
  KeyMap = {
    "h": direction.W, "j": direction.S, "k": direction.N, "l": direction.E,
    "y": direction.NW, "u": direction.NE, "b": direction.SW, "n": direction.SE
  }

  def __init__(self):
    self._target = (1, 1)
    self._center = (10, 10)
    self._console = Console()

  def run(self):
    while True:
      self.update()

  def update(self):
    self.render()
    key = self._console.getKey()
    self.moveTarget(self.KeyMap.get(key, (0, 0)))

  def moveTarget(self, dir):
    self._target = coord.sum(self._target, dir)

  def render(self):
    self._console.clear()
    self._console.move(self._center).write('@')
    self._console.move(self._target).write('X')
    for c in coord.line(self._center, self._target):
      self._console.move(c).write('.')
    self._console.move(self._target)

if __name__ == '__main__':
  LineDemo().run()
