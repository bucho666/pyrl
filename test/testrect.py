import unittest
from rect import Rect
from coord import Coord
from size import Size

class TestRect(unittest.TestCase):
  def testProperty(self):
    r = Rect(Coord(1, 2), Size(3, 4))
    self.assertEqual(r.x, 1)
    self.assertEqual(r.y, 2)
    self.assertEqual(r.width, 3)
    self.assertEqual(r.height, 4)
    self.assertEqual(r.left, 1)
    self.assertEqual(r.top, 2)
    self.assertEqual(r.right, 3)
    self.assertEqual(r.bottom, 5)
    self.assertEqual(r.coord, Coord(1, 2))
    self.assertEqual(r.size, Size(3, 4))

  def testEqual(self):
    r = Rect(Coord(1, 2), Size(3, 4))
    self.assertEqual(r, Rect(Coord(1, 2), Size(3, 4)))
    d = {r: 42}
    self.assertEqual(d[Rect(Coord(1, 2), Size(3, 4))], 42)

  def testVerticalSplit(self):
    r = Rect(Coord(1, 2), Size(9, 9))
    (left, right) = r.verticalSplit(4)
    self.assertEqual(left, Rect(Coord(1, 2), Size(4, 9)))
    self.assertEqual(right, Rect(Coord(4, 2), Size(6, 9)))

  def testHorizontalSplit(self):
    r = Rect(Coord(1, 2), Size(9, 9))
    (top, bottom) = r.horizontalSplit(4)
    self.assertEqual(top, Rect(Coord(1, 2), Size(9, 4)))
    self.assertEqual(bottom, Rect(Coord(1, 5), Size(9, 6)))
