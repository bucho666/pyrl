# -*- coding: utf-8 -*-
from coord import Coord
import direction

class Vector(object):
  def __init__(self, coord, slope):
    self._coord = coord
    self._slope = slope

  def __add__(self, other):
    return Vector(Coord(self.x + other.x, self.y + other.y), self._slope)

  def __sub__(self, other):
    return Vector(Coord(self.x - other.x, self.y - other.y), self._slope)

  @property
  def x(self):
    return round(self._coord.x)

  @property
  def y(self):
    return round(self._coord.y)

  def step(self):
    return Vector(Coord(self._coord.x + self._slope, self.y + 1), self._slope)

  def toOctant(self, center, octant):
    diff = self._coord - center
    if octant == 1: return Vector(center + Coord(diff.y, diff.x), self._slope)
    if octant == 2: return Vector(center + Coord(-diff.x, diff.y), self._slope)
    if octant == 3: return Vector(center + Coord(-diff.y, diff.x), self._slope)
    if octant == 4: return Vector(center + Coord(diff.x, -diff.y), self._slope)
    if octant == 5: return Vector(center + Coord(diff.y, -diff.x), self._slope)
    if octant == 6: return Vector(center + Coord(-diff.x, -diff.y), self._slope)
    if octant == 7: return Vector(center + Coord(-diff.y, -diff.x), self._slope)
    return self

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
      current = current + direction.E

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
      current = current + direction.E
    if lastVisible:
      result.append(self.viewPair(lastVisible, current + direction.W))
    return result

  def viewPair(self, begin, end):
    return (Vector(begin, self.calculateSlope(begin)),
            Vector(end, self.calculateSlope(end)))

  def isInsight(self, vector):
    distance = vector - self._start
    return distance.x ** 2 + distance.y ** 2 < self._radius

  def calculateSlope(self, coord):
    distance = coord - self._start
    return distance.x / distance.y
