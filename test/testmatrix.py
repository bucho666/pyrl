import unittest
from matrix import Matrix
import coord

class TestMatrix(unittest.TestCase):
  def testSize(self):
    m = Matrix((2, 3))
    self.assertEqual(m.width, 2)
    self.assertEqual(m.height, 3)

  def testPutAndAt(self):
    m = Matrix((2, 3))
    c = (1, 2)
    self.assertEqual(m.at((1, 2)), None)
    m.put(c, 42)
    self.assertEqual(m.at((1, 2)), 42)

  def testIterate(self):
    m = Matrix((2, 3))
    self.assertEqual([line for line in m], [
      (0, 0), (1, 0),
      (0, 1), (1, 1),
      (0, 2), (1, 2)])

  def testInitialize(self):
    m = Matrix((2, 3), 42)
    self.assertTrue(all([m.at(c) == 42 for c in m]))

  def testFill(self):
    m = Matrix((2, 3))
    self.assertTrue(all([m.at(c) == None for c in m]))
    m.fill(42)
    self.assertTrue(all([m.at(c) == 42 for c in m]))

  def testOutBound(self):
    m = Matrix((2, 3))
    self.assertTrue(m.isOutBound((2, 3)))
    self.assertTrue(m.isOutBound((2, 0)))
    self.assertTrue(m.isOutBound((0, 3)))
    self.assertFalse(m.isOutBound((0, 0)))
    self.assertFalse(m.isOutBound((1, 2)))

  def testInBound(self):
    m = Matrix((2, 3))
    self.assertFalse(m.isInBound((2, 3)))
    self.assertFalse(m.isInBound((2, 0)))
    self.assertFalse(m.isInBound((0, 3)))
    self.assertTrue(m.isInBound((0, 0)))
    self.assertTrue(m.isInBound((1, 2)))

  def testLine(self):
    m = Matrix((4, 3))
    for x in range(4):
      m.put((x, 1), x * 2)
    expected = [0, 2, 4, 6]
    self.assertEqual(m.line(1), expected)
    expected[1] = 42
    self.assertEqual(m.line(1), [0, 2, 4, 6])

  def testLines(self):
    m = Matrix((2, 3))
    m.put((0, 0), 42);
    m.put((1, 1), '@');
    m.put((0, 2), 0.2);
    self.assertEqual([line for line in m.lines], [[42, None], [None, '@'], [0.2, None]])

