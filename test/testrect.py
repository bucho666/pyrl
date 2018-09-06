import unittest
from rect import Rect

class TestRect(unittest.TestCase):
  def testProperty(self):
    r = Rect((1, 2), (3, 4))
    self.assertEqual(r.x, 1)
    self.assertEqual(r.y, 2)
    self.assertEqual(r.width, 3)
    self.assertEqual(r.height, 4)
    self.assertEqual(r.left, 1)
    self.assertEqual(r.top, 2)
    self.assertEqual(r.right, 3)
    self.assertEqual(r.bottom, 5)
    self.assertEqual(r.coord, (1, 2))
    self.assertEqual(r.size, (3, 4))

  def testEqual(self):
    r = Rect((1, 2), (3, 4))
    self.assertEqual(r, Rect((1, 2), (3, 4)))
    d = {r: 42}
    self.assertEqual(d[Rect((1, 2), (3, 4))], 42)

  def testVerticalSplit(self):
    r = Rect((1, 2), (9, 9))
    (left, right) = r.verticalSplit(4)
    self.assertEqual(left, Rect((1, 2), (4, 9)))
    self.assertEqual(right, Rect((4, 2), (6, 9)))

  def testHorizontalSplit(self):
    r = Rect((1, 2), (9, 9))
    (top, bottom) = r.horizontalSplit(4)
    self.assertEqual(top, Rect((1, 2), (9, 4)))
    self.assertEqual(bottom, Rect((1, 5), (9, 6)))

  def testFrame(self):
    r = Rect((1, 2), (3, 4))
    frame = [c for c in r.frame]
    expect = [
      (1, 2), (1, 5),
      (2, 2), (2, 5),
      (3, 2), (3, 5),
      (1, 3), (3, 3),
      (1, 4), (3, 4),
      ]
    self.assertTrue(all([a == b for a, b in zip(frame, expect)]))

  def testReduce(self):
    r = Rect((1, 2), (3, 4))
    self.assertEqual(r.reduce(1), Rect((1, 2), (2, 3)))
    self.assertEqual(r.reduce(2), Rect((1, 2), (1, 2)))
    self.assertEqual(r.reduce(3), Rect((1, 2), (0, 1)))

  def testShurink(self):
    r = Rect((1, 2), (3, 4))
    self.assertEqual(r.shurink(1), Rect((2, 3), (1, 2)))

  def testIterate(self):
    r = Rect((1, 2), (3, 4))
    result = [c for c in r]
    expect = [
        (1, 2), (2, 2), (3, 2),
        (1, 3), (2, 3), (3, 3),
        (1, 4), (2, 4), (3, 4),
        (1, 5), (2, 5), (3, 5),
        ]
    self.assertTrue(all([a == b for a, b in zip(result, expect)]))
