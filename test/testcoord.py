import unittest
import coord

class TestCoord(unittest.TestCase):
  def testSumAndSub(self):
    self.assertEqual(coord.sum((1, 2), (3, 4)), (4, 6))
    self.assertEqual(coord.sub((3, 4), (1, 2)), (2, 2))

  def testMultiSumAndSub(self):
    self.assertEqual(coord.sum((1, 2), (3, 4), (5, 6)), (9, 12))
    self.assertEqual(coord.sub((5, 6), (3, 4), (1, 2)), (1, 0))

