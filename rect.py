from size import Size
from coord import Coord

class Rect(object):
  def __init__(self, coord, size):
    self._coord = coord
    self._size = size

  def __eq__(self, other):
    return self.coord == other.coord and self.size == other.size

  def __hash__(self):
    return hash((self.x, self.y, self.width, self.height))

  def __iter__(self):
    for y in range(self.top, self.bottom + 1):
      for x in range(self.left, self.right + 1):
        yield Coord(x, y)

  @property
  def x(self):
    return self._coord.x

  @property
  def y(self):
    return self._coord.y

  @property
  def width(self):
    return self._size.width

  @property
  def height(self):
    return self._size.height

  @property
  def left(self):
    return self._coord.x

  @property
  def top(self):
    return self._coord.y

  @property
  def right(self):
    return self._coord.x + self._size.width - 1

  @property
  def bottom(self):
    return self._coord.y + self._size.height - 1

  @property
  def coord(self):
    return self._coord

  @property
  def size(self):
    return self._size

  @property
  def frame(self):
    for x in range(self.left, self.right + 1):
      yield Coord(x, self.top)
      yield Coord(x, self.bottom)
    for y in range(self.top, self.bottom + 1):
      if (y != self.top and y != self.bottom):
        yield Coord(self.left, y)
        yield Coord(self.right, y)

  def verticalSplit(self, width):
    left = Rect(self.coord, Size(width, self.height))
    right = Rect(Coord(self.x + width - 1, self.y), Size(self.width - width + 1, self.height))
    return (left, right)

  def horizontalSplit(self, height):
    top = Rect(self.coord, Size(self.width, height))
    bottom = Rect(Coord(self.x, self.y + height- 1), Size(self.width, self.height - height+ 1))
    return (top, bottom)

  def reduce(self, value):
    return Rect(self.coord, self.size - Size(value, value))
