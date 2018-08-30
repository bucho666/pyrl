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

  def testFrame(self):
    r = Rect(Coord(1, 2), Size(3, 4))
    frame = [c for c in r.frame]
    expect = [
      Coord(1, 2), Coord(1, 5),
      Coord(2, 2), Coord(2, 5),
      Coord(3, 2), Coord(3, 5),
      Coord(1, 3), Coord(3, 3),
      Coord(1, 4), Coord(3, 4),
      ]
    self.assertTrue(all([a == b for a, b in zip(frame, expect)]))

  def testReduce(self):
    r = Rect(Coord(1, 2), Size(3, 4))
    self.assertEqual(r.reduce(1), Rect(Coord(1, 2), Size(2, 3)))
    self.assertEqual(r.reduce(2), Rect(Coord(1, 2), Size(1, 2)))
    self.assertEqual(r.reduce(3), Rect(Coord(1, 2), Size(0, 1)))

  def testShurink(self):
    r = Rect(Coord(1, 2), Size(3, 4))
    self.assertEqual(r.shurink(1), Rect(Coord(2, 3), Size(1, 2)))

  def testIterate(self):
    r = Rect(Coord(1, 2), Size(3, 4))
    result = [c for c in r]
    expect = [
        Coord(1, 2), Coord(2, 2), Coord(3, 2),
        Coord(1, 3), Coord(2, 3), Coord(3, 3),
        Coord(1, 4), Coord(2, 4), Coord(3, 4),
        Coord(1, 5), Coord(2, 5), Coord(3, 5),
        ]
    self.assertTrue(all([a == b for a, b in zip(result, expect)]))
