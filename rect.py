class Rect(object):
  def __init__(self, coord, size):
    (self._x, self._y), (self._width, self._height) = coord, size

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y and self.width == other.width and self.height == other.height

  def __hash__(self):
    return hash((self.x, self.y, self.width, self.height))

  def __iter__(self):
    for y in range(self.top, self.bottom + 1):
      for x in range(self.left, self.right + 1):
        yield (x, y)

  @property
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y

  @property
  def width(self):
    return self._width

  @property
  def height(self):
    return self._height

  @property
  def left(self):
    return self._x

  @property
  def top(self):
    return self._y

  @property
  def right(self):
    return self._x + self._width - 1

  @property
  def bottom(self):
    return self.y + self._height - 1

  @property
  def coord(self):
    return (self._x, self._y)

  @property
  def size(self):
    return (self._width, self._height)

  @property
  def frame(self):
    for x in range(self.left, self.right + 1):
      yield (x, self.top)
      yield (x, self.bottom)
    for y in range(self.top, self.bottom + 1):
      if (y != self.top and y != self.bottom):
        yield (self.left, y)
        yield (self.right, y)

  def verticalSplit(self, width):
    left = Rect(self.coord, (width, self.height))
    right = Rect((self._x + width - 1, self._y), (self._width - width + 1, self._height))
    return (left, right)

  def horizontalSplit(self, height):
    top = Rect(self.coord, (self._width, height))
    bottom = Rect((self._x, self._y + height - 1), (self._width, self._height - height + 1))
    return (top, bottom)

  def reduce(self, value):
    return Rect(self.coord, (self._width - value, self._height - value))

  def shurink(self, value):
    return Rect((self._x + value, self._y + value), (self._width - (value * 2), self._height - (value * 2)))
