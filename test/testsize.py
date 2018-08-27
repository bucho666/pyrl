import unittest
from size import Size

class TestSize(unittest.TestCase):
  def testProperty(self):
    size = Size(1, 2)
    self.assertEqual(size.width, 1)
    self.assertEqual(size.height, 2)

  def testEqual(self):
    self.assertEqual(Size(1, 2), Size(1, 2))
    d = {Size(3, 4): 42}
    self.assertEqual(d[Size(3, 4)], 42)

  def testPlusMinus(self):
    self.assertEqual(Size(1, 2) + Size(3, 4), Size(4, 6))
    self.assertEqual(Size(3, 4) - Size(1, 2), Size(2, 2))

  def testStr(self):
    self.assertEqual(str(Size(1, 2)), "(1, 2)")


