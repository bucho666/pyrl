# -*- coding: utf-8 -*-
import coord
import direction

class Vector(object):
  def __init__(self, point, slope):
    self._x, self._y = point
    self._slope = slope

  def __add__(self, other):
    x, y = other
    return Vector((self._x + x, self._y + y), self._slope)

  def __sub__(self, other):
    x, y = other
    return Vector((self._x - x, self._y - y), self._slope)

  @property
  def x(self):
    return round(self._x)

  @property
  def y(self):
    return round(self._y)

  @property
  def coord(self):
    return (self._x, self._y)

  def step(self):
    return Vector((self._x + self._slope, self._y + 1), self._slope)

  def toOctant(self, center, octant):
    dx, dy = coord.sub((self.x, self.y), center)
    if octant == 0: return coord.sum(center, (dx, dy))
    if octant == 1: return coord.sum(center, (dy, dx))
    if octant == 2: return coord.sum(center, (-dx, dy))
    if octant == 3: return coord.sum(center, (-dy, dx))
    if octant == 4: return coord.sum(center, (dx, -dy))
    if octant == 5: return coord.sum(center, (dy, -dx))
    if octant == 6: return coord.sum(center, (-dx, -dy))
    if octant == 7: return coord.sum(center, (-dy, -dx))
    raise ValueError("invalid octant")

class Fov(object):
  def __init__(self, isVisible, radius=6):
    self._isVisible = isVisible
    self._radius = (radius + 1) ** 2
    self._visibles = set()
    self._start = None

  def compute(self, start):
    self._start = start
    self._visibles = set([start])
    for octant in range(8):
      self.scan(Vector(start, 0), Vector(start, 1), octant)
    return self._visibles

  def scan(self, begin, end, octant):
    begin, end = begin.step(), end.step()
    self.scanLine(begin, end, octant)
    for view in self.splitView(begin, end, octant):
      self.scan(*view, octant)

  def scanLine(self, begin, end, octant):
    current = begin
    while(current.x <= end.x):
      if self.isInsight(current):
        self._visibles.add(current.toOctant(self._start, octant))
      current += direction.E

  def splitView(self, begin, end, octant):
    result = []
    current = begin
    lastVisible = None
    while current.x <= end.x:
      visible = self._isVisible(current.toOctant(self._start, octant))
      if visible and not lastVisible:
        lastVisible = current
      elif not visible and lastVisible:
        result.append(self.viewPair(lastVisible, current + direction.W))
        lastVisible = None
      current += direction.E
    if lastVisible:
      result.append(self.viewPair(lastVisible, current + direction.W))
    return result

  def viewPair(self, begin, end):
    return (Vector(begin.coord, self.calculateSlope(begin)),
            Vector(end.coord, self.calculateSlope(end)))

  def isInsight(self, vector):
    dx, dy = (vector - self._start).coord
    return dx ** 2 + dy ** 2 < self._radius

  def calculateSlope(self, vector):
    distance = vector - self._start
    return distance.x / distance.y
