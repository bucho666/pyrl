import math

class Coord(object):
  def __init__(self, x, y):
    self._x = x
    self._y = y

  @property
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __hash__(self):
    return hash((self._x, self._y))

  def __add__(self, other):
    return Coord(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    return Coord(self.x - other.x, self.y - other.y)

  def __str__(self):
    return str((self._x, self._y))

  def toLine(self, to):
    dx, dy = abs(to.x - self.x), abs(to.y - self.y)
    sx = 1 if self.x < to.x else -1
    sy = 1 if self.y < to.y else -1
    x, y, error = self.x, self.y, dx - dy
    while True:
      error2 = error * 2
      if error2 > -dy:
        error -= dy
        x += sx
      if error2 < dx:
        error += dx
        y += sy
      if x == to.x and y == to.y: break
      yield Coord(x, y)
