# -*- coding: utf-8 -*-
import random
from size import Size
from matrix import Matrix
from rect import Rect
from coord import Coord

class RoomSizeRange(object):
  def __init__(self, min, max):
    self._min = min
    self._max = max

  @property
  def min(self):
    return self._min

  @property
  def max(self):
    return self._max

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

  def randomSize(self):
    widthCandidate = [w for w in range(self._min.width, self._max.width + 1) if w % 2]
    heightCandidate = [h for h in range(self._min.height, self._max.height+ 1) if h % 2]
    return Size(random.choice(widthCandidate), random.choice(heightCandidate))

class Generator(object):
  def __init__(self, size):
    self._map = Matrix(size, '#')
    self._area = [Rect(Coord(0, 0), size)]
    self._room = []
    self._roomSize = RoomSizeRange(Size(7, 5), Size(13, 7))
    self._entrance = []
    self._entranceMax = 4

  @property
  def area(self):
    return self._area[:]

  @property
  def room(self):
    return self._room[:]

  def generate(self):
    self.splitAreas()
    self.makeRoom()
    return self

  def splitAreas(self):
    lastSize = 0
    while lastSize != len(self._area):
      lastSize = len(self._area)
      for area in self._area:
        if self.verticalSplitArea(area): continue
        self.horizontalSplitArea(area)

  def makeRoom(self):
    for area in self.area:
      self.makeRoomInArea(area)
    for room in self._room:
      self.putRoom(room)
      self.makeRoomEntrance(room)

  def putRoom(self, room):
    for c in room.frame:
      self._map.put(c, '#')
    for c in room.reduce(1):
      self._map.put(c, '.')

  def makeRoomEntrance(self, room):
    candidate = []
    for c in room.frame:
      if c.x == 0 or c.y == 0: continue
      if c.x == self._map.width - 1 or c.y == self._map.height - 1: continue
      if c.x % 2 == 0 and c.y % 2 == 0: continue
      candidate.append(c)
    for c in range(random.randrange(1, self._entranceMax + 1)):
      e = random.choice(candidate)
      self._entrance.append(e)
      candidate.remove(e)

  def makeRoomInArea(self, area):
    roomArea = area.reduce(1)
    size = RoomSizeRange(self._roomSize.min, roomArea.size).randomSize()
    x = random.choice([x for x in range(roomArea.x, roomArea.right - size.width + 2) if x % 2 == 0])
    y = random.choice([y for y in range(roomArea.y, roomArea.bottom - size.height + 2) if y % 2 == 0])
    room = Rect(Coord(x, y), size)
    self._room.append(room)

  def verticalSplitArea(self, area):
    if area.width < self._roomSize.maxWidth * 2: return False
    self._area.remove(area)
    min = self._roomSize.minWidth + 2
    max = area.width - self._roomSize.minWidth - 2
    split = random.choice([v for v in range(min, max + 1) if v % 2])
    self._area.extend(area.verticalSplit(split))
    return True

  def  horizontalSplitArea(self, area):
    if area.height < self._roomSize.maxHeight * 2: return False
    self._area.remove(area)
    min = self._roomSize.minHeight + 1
    max = area.height - self._roomSize.minHeight - 1
    split = random.choice([v for v in range(min, max + 1) if v % 2])
    self._area.extend(area.horizontalSplit(split))
    return True

if __name__ == '__main__':
  size = Size(79, 21)
  g = Generator(size).generate()
  m = Matrix(size, ' ')
  for area in g.area:
    for c in area.frame:
      print(c)
      m.put(c, '.')
  for room in g.room:
    for c in room.frame:
      m.put(c, '#')
  for c in g._entrance:
    m.put(c, '+')

  for line in m.lines:
    print(''.join(line))
