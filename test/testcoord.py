import unittest
from coord import Coord

class TestCoord(unittest.TestCase):
  def testEqual(self):
    a = Coord(1, 2)
    b = Coord(1, 2)
    self.assertEqual(a, b)
    d = {Coord(1, 2): 42}
    self.assertEqual(d[Coord(1, 2)], 42)

  def testPlusMinus(self):
    self.assertEqual(Coord(1, 2) + Coord(3, 4), Coord(4, 6))
    self.assertEqual(Coord(3, 4) - Coord(1, 2), Coord(2, 2))
