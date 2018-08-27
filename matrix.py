from coord import Coord

class Matrix(object):
  def __init__(self, size, initial=None):
    self._map = [[initial for x in range(size.width)] for y in range(size.height)]

  @property
  def height(self):
    return len(self._map)

  @property
  def width(self):
    return len(self._map[0])

  def __iter__(self):
    for y in range(self.height):
      for x in range(self.width):
        yield Coord(x, y)

  def at(self, coord):
    return self._map[coord.y][coord.x]

  def put(self, coord, value):
    self._map[coord.y][coord.x] = value

  def fill(self, value):
    self._map = [[value for x in range(self.width)] for y in range(self.height)]

  def isOutBound(self, coord):
    return coord.x < 0 or coord.y < 0 or coord.x >= self.width or coord.y >= self.height

  def isInBound(self, coord):
    return not self.isOutBound(coord)

  def line(self, y):
    return self._map[y]

  @property
  def lines(self):
    for line in self._map:
      yield line
