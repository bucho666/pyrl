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
    self.assertEqual([line for line in m], [
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

  def testLine(self):
    m = Matrix(Size(4, 3))
    for x in range(4):
      m.put(Coord(x, 1), x * 2)
    expected = [0, 2, 4, 6]
    self.assertEqual(m.line(1), expected)
    expected[1] = 42
    self.assertEqual(m.line(1), [0, 2, 4, 6])

  def testLines(self):
    m = Matrix(Size(2, 3))
    m.put(Coord(0, 0), 42);
    m.put(Coord(1, 1), '@');
    m.put(Coord(0, 2), 0.2);
    self.assertEqual([line for line in m.lines], [[42, None], [None, '@'], [0.2, None]])

