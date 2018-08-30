# -*- coding: utf-8 -*-
import random
from size import Size
from matrix import Matrix
from rect import Rect
from coord import Coord
import direction

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

class TileType(object):
  STOP_DIG = 1 << 1
  WALL = 1 << 2
  DOOR = 1 << 3

  def __init__(self, ch):
    self._ch = ch
    self._flag = 0

  @property
  def ch(self):
    return self._ch

  @property
  def isStopDig(self):
    return self._flag & self.STOP_DIG

  @property
  def isWall(self):
    return self._flag & self.WALL

  @property
  def isDoor(self):
    return self._flag & self.DOOR

  def stopDig(self):
    self._flag |= self.STOP_DIG
    return self

  def wall(self):
    self._flag |= self.WALL
    return self

  def door(self):
    self._flag |= self.DOOR
    return self

class Tile(object):
  NULL = TileType('#').wall()
  ROOM = TileType('.')
  WALL = TileType('#').stopDig().wall()
  DOOR = TileType('+')
  CORRIDOR = TileType(' ').stopDig()
  DEADEND = TileType('x')

class Generator(object):
  def __init__(self, size):
    self._map = Matrix(size, Tile.NULL)
    self._area = [Rect(Coord(0, 0), size)]
    self._roomSize = RoomSizeRange(Size(7, 5), Size(13, 7))
    self._entranceMax = 4
    self._deadend = 2
    self._room = []
    self._entrance = []
    self._diged = Matrix(size, False)
    self._deadends = []

  def __iter__(self):
    for c in self._map:
      yield (c, self._map.at(c))

  @property
  def area(self):
    return self._area[:]

  @property
  def room(self):
    return self._room[:]

  @property
  def deadends(self):
    return self._deadends[:]

  def setEntranceMax(self, value):
    self._entranceMax = value
    return self

  def setDeadEnd(self ,value):
    self._deadend = value
    return self

  def setRoomSizeRange(self, small, big):
    self._roomSize = RoomSizeRange(small, big)
    return self

  def toString(self):
    return '\n'.join([''.join([t.ch for t in line]) for line in self._map.lines])

  def generate(self):
    self.splitAreas()
    self.makeRoom()
    self.digCorridor()
    self.removeDeadEnd()
    return self

  def splitAreas(self):
    lastSize = 0
    while lastSize != len(self._area):
      lastSize = len(self._area)
      for area in self._area:
        if self.verticalSplitArea(area): continue
        self.horizontalSplitArea(area)

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

  def makeRoom(self):
    for area in self._area:
      self.makeRoomInArea(area)
    for room in self._room:
      self.putRoom(room)
      self.makeRoomEntrance(room)

  def makeRoomInArea(self, area):
    roomArea = area.reduce(1)
    size = RoomSizeRange(self._roomSize.min, roomArea.size).randomSize()
    x = random.choice([x for x in range(roomArea.x, roomArea.right - size.width + 2) if x % 2 == 0])
    y = random.choice([y for y in range(roomArea.y, roomArea.bottom - size.height + 2) if y % 2 == 0])
    room = Rect(Coord(x, y), size)
    self._room.append(room)

  def putRoom(self, room):
    for c in room:
      self._map.put(c, Tile.ROOM)
    for c in room.frame:
      self._map.put(c, Tile.WALL)

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
      self._map.put(e, Tile.DOOR)
      candidate.remove(e)

  def digCorridor(self):
    for y in range(1, self._map.height, 2):
      for x in range(1, self._map.width, 2):
        self.digAround(Coord(x, y))

  def startDigCorridor(self, coord, dir):
    step = (coord + dir, coord + dir + dir)
    if any([self._map.isOutBound(c) for c in step]): return
    if any([self._map.at(c).isStopDig for c in step]): return
    if any([self._diged.at(c) for c in step]): return
    for c in step:
      self._diged.put(c, True)
      if self._map.at(c) == Tile.NULL:
        self._map.put(c, Tile.CORRIDOR)
    self.digAround(step[1])

  def digAround(self, coord):
    dirs = list(direction.CROSS)
    random.shuffle(dirs)
    for d in dirs:
      self.startDigCorridor(coord, d)

  def removeDeadEnd(self):
    self.updateDeadEnd()
    while(self._deadend < len(self._deadends)):
      de = random.choice(self._deadends)
      self._deadends.remove(de)
      self.fillDeadEnd(de)

  def updateDeadEnd(self):
    for y in range(1, self._map.height, 2):
      for x in range(1, self._map.width, 2):
        c = Coord(x, y)
        if self._map.at(c).isWall: continue
        if self.isDeadEnd(c):
          self._deadends.append(c)

  def fillDeadEnd(self, coord):
    if not self.isDeadEnd(coord): return
    self._map.put(coord, Tile.NULL)
    for d in direction.CROSS:
      step = coord + d
      if self._map.at(step).isWall: continue
      self.fillDeadEnd(step)
      break
    for de in self._deadends:
      self._map.put(de, Tile.DEADEND)

  def isDeadEnd(self, coord):
    wall = 0
    for d in direction.CROSS:
      if self._map.at(coord + d).isWall:
        wall += 1
    return wall == 3

if __name__ == '__main__':
  size = Size(79, 21)
  g = Generator(size).setDeadEnd(3).generate()
  m = Matrix(size, ' ')
  for (c, t) in g:
    m.put(c, t.ch)
  for room in g.room:
    inside = room.shurink(1)
    for c in inside:
      if random.randint(0, 2):
        m.put(c, random.choice('abcdefghijklmnopqrstuvwxyz'))
  deadends = [de for de in g.deadends]
  random.shuffle(deadends)
  m.put(deadends[0], '>')
  m.put(deadends[1], '<')
  m.put(deadends[2], '$')
  for line in m.lines:
    print(''.join([c for c in line]))
