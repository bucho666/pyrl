class Size(object):
  def __init__(self, width, height):
    self._width = width
    self._height = height

  @property
  def width(self):
    return self._width

  @property
  def height(self):
    return self._height

  def __eq__(self, other):
    return self.width == other.width and self.height and other.height

  def __hash__(self):
    return hash((self._width, self._width))
