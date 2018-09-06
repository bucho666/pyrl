import coord
from size import Size

class Matrix(object):
  def __init__(self, size, initial=None):
    w, h = size
    self._map = [[initial for x in range(w)] for y in range(h)]

  def __iter__(self):
    for y in range(self.height):
      for x in range(self.width):
        yield (x, y)

  @property
  def height(self):
    return len(self._map)

  @property
  def width(self):
    return len(self._map[0])

  @property
  def size(self):
    return Size(self.width, self.height)

  @property
  def lines(self):
    for line in self._map:
      yield line

  def at(self, coord):
    x, y = coord
    return self._map[y][x]

  def put(self, coord, value):
    x, y = coord
    self._map[y][x] = value

  def fill(self, value):
    self._map = [[value for x in range(self.width)] for y in range(self.height)]

  def isOutBound(self, coord):
    x, y = coord
    return x < 0 or y < 0 or x >= self.width or y >= self.height

  def isInBound(self, coord):
    return not self.isOutBound(coord)

  def line(self, y):
    return self._map[y]

