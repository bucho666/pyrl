# -*- coding: utf-8 -*-
import parentpath
import random
import coord
from console import Console
from console import Color

class Walk(object):
  KeyMap = {
    "h": (-1,  0), "j": (0,  1), "k": (0, -1), "l": (1, 0),
    "y": (-1, -1), "u": (1, -1), "b": (-1, 1), "n": (1, 1)
  }

  def __init__(self):
    self._coord = (1, 1)
    self._console = Console().colorOn().nonBlocking()

  def run(self):
    self.render()
    interval = int(1000/30)
    while True:
      self.update()
      self._console.sleep(interval)

  def update(self):
    key = self._console.getKey()
    coord.sum(self._coord, Walk.KeyMap.get(key, (0, 0)))
    self.render()

  def render(self):
    self._console.clear()
    self._console.move((1, 2)).write("+", Color.LIGHT_YELLOW)
    self._console.move((3, 4)).write("T", Color.GREEN, Color.BLUE)
    self._console.move((5, 6)).write("*", Color.LIGHT_YELLOW, Color.GREEN)
    self._console.move((7, 8)).write("&", random.choice(list(Color.LIST)))
    self._console.move(self._coord).write("@", Color.LIGHT_YELLOW).move(self._coord)

if __name__ == '__main__':
  Walk().run()
