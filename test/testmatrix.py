import unittest
from matrix import Matrix
from size import Size
from coord import Coord

class TestMatrix(unittest.TestCase):
  def testSize(self):
    m = Matrix(Size(2, 3))
    self.assertEqual(m.width, 2)
    self.assertEqual(m.height, 3)

  def testPutAndAt(self):
    m = Matrix(Size(2, 3))
    c = Coord(1, 2)
    self.assertEqual(m.at(Coord(1, 2)), None)
    m.put(c, 42)
    self.assertEqual(m.at(Coord(1, 2)), 42)

  def testIterate(self):
    m = Matrix(Size(2, 3))
    self.assertEqual([c for c in m], [
      Coord(0, 0), Coord(1, 0),
      Coord(0, 1), Coord(1, 1),
      Coord(0, 2), Coord(1, 2)])

  def testInitialize(self):
    m = Matrix(Size(2, 3), 42)
    self.assertTrue(all([m.at(c) == 42 for c in m]))

  def testFill(self):
    m = Matrix(Size(2, 3))
    self.assertTrue(all([m.at(c) == None for c in m]))
    m.fill(42)
    self.assertTrue(all([m.at(c) == 42 for c in m]))

  def testOutBound(self):
    m = Matrix(Size(2, 3))
    self.assertTrue(m.isOutBound(Coord(2, 3)))
    self.assertTrue(m.isOutBound(Coord(2, 0)))
    self.assertTrue(m.isOutBound(Coord(0, 3)))
    self.assertFalse(m.isOutBound(Coord(0, 0)))
    self.assertFalse(m.isOutBound(Coord(1, 2)))

  def testInBound(self):
    m = Matrix(Size(2, 3))
    self.assertFalse(m.isInBound(Coord(2, 3)))
    self.assertFalse(m.isInBound(Coord(2, 0)))
    self.assertFalse(m.isInBound(Coord(0, 3)))
    self.assertTrue(m.isInBound(Coord(0, 0)))
    self.assertTrue(m.isInBound(Coord(1, 2)))
