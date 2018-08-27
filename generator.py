# -*- coding: utf-8 -*-
import random
from size import Size
from matrix import Matrix
from rect import Rect
from coord import Coord


class SizeRange(object):
  def __init__(self, min, max):
    self._min = min
    self._max = max

  @property
  def minWidth(self):
    return self._min.width

  @property
  def minHeight(self):
    return self._min.height

  @property
  def maxWidth(self):
    return self._max.width

  @property
  def maxHeight(self):
    return self._max.height

class Generator(object):
  def __init__(self, size):
    self._map = Matrix(size, '#')
    self._area = [Rect(Coord(0, 0), size)]
    self._roomSize = SizeRange(Size(5, 3), Size(13, 7))

  @property
  def area(self):
    return self._area[:]

  def generate(self):
    for c in range(10):
      self.splitArea()
    return self

  def splitArea(self):
    lastSize = 0
    while len(self._area) != lastSize:
      lastSize = len(self._area)
      for area in self._area:
        random.choice([self.verticalSplitArea, self.horizontalSplitArea ])(area)

  def verticalSplitArea(self, area):
    if area.width < self._roomSize.maxWidth * 2: return
    self._area.remove(area)
    self._area.extend(area.verticalSplit(random.randrange(self._roomSize.minWidth + 2,
      area.width - self._roomSize.minWidth - 2)))

  def  horizontalSplitArea(self, area):
    if area.height < self._roomSize.maxHeight * 2: return
    self._area.remove(area)
    self._area.extend(area.horizontalSplit(random.randrange(self._roomSize.minHeight + 2,
      area.height - self._roomSize.minHeight - 2)))

if __name__ == '__main__':
  size = Size(79, 21)
  g = Generator(size).generate()
  m = Matrix(size, ' ')
  for area in g.area:
    for c in area.frame:
      m.put(c, '$')
  for line in m.lines:
    print(''.join(line))
