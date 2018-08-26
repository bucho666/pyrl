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
