class Size(object):
  def __init__(self, width, height):
    self._width = width
    self._height = height

  def __eq__(self, other):
    return self.width == other.width and self.height and other.height

  def __hash__(self):
    return hash((self._width, self._width))

  def __add__(self, other):
    return Size(self.width + other.width, self.height + other.height)

  def __sub__(self, other):
    return Size(self.width - other.width, self.height - other.height)

  def __str__(self):
    return str((self._width, self._height))

  @property
  def width(self):
    return self._width

  @property
  def height(self):
    return self._height



