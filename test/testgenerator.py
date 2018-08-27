# -*- coding: utf-8 -*-
from generator import SizeRange
from size import Size
import unittest

class TestGenerator(unittest.TestCase):
  def testSizeRangeProperty(self):
    sr = SizeRange(Size(1, 2), Size(3, 4))
    self.assertEqual(sr.minWidth, 1)
    self.assertEqual(sr.minHeight, 2)
    self.assertEqual(sr.maxWidth, 3)
    self.assertEqual(sr.maxHeight, 4)

